from celery import shared_task
from django.db import connections, models, transaction
from datetime import timedelta
from django.utils import timezone
import logging

logger = logging.getLogger('celery')

@shared_task(name='archival_api.services.archival_service')
def archival_service():
    try:
        # Get the archival configuration (e.g., from the ArchivalConfig table)
        from archival_api.models import ArchivalConfig
        
        # Get the current date
        now = timezone.now()

        # Loop through each table in the config that needs to be archived
        configs = ArchivalConfig.objects.all()
        
        for config in configs:
            table_name = config.table_name
            archival_period_days = config.archival_period_days

            # Calculate the archival date (N days ago)
            archival_date = now - timedelta(days=archival_period_days)

            # Fetch records older than 'archival_date' from the 'primary_db'
            with connections['primary_db'].cursor() as cursor:
                # Dynamically fetch column names for the table from the primary DB
                cursor.execute(f"DESCRIBE {table_name};")
                columns = [column[0] for column in cursor.fetchall()]  # column[0] contains column names

                # Fetch records older than 'archival_date'
                query = f"""
                    SELECT {', '.join(columns)} FROM {table_name} 
                    WHERE created_on <= %s;
                """
                cursor.execute(query, [archival_date])
                rows_to_archive = cursor.fetchall()

                # Add archived on field for rows to be archived
                columns.append('archived_on')
                # Use the map function to add `archive_date` to each row
                rows_to_archive = list(map(lambda row: row + (archival_date,), rows_to_archive))

            if rows_to_archive:
                logger.info(f"Found {len(rows_to_archive)} records to archive from table {table_name}")

                # Insert records into archived database (archived_db)
                with connections['archived_db'].cursor() as cursor:
                    # Prepare the insert query dynamically
                    placeholders = ", ".join(["%s"] * len(columns))
                    insert_query = f"""
                        INSERT INTO archival_api_archived{table_name} ({', '.join(columns)}) 
                        VALUES ({placeholders});
                    """
                    cursor.executemany(insert_query, rows_to_archive)

                
                # Optionally, delete the records from the primary database
                with connections['primary_db'].cursor() as cursor:
                    delete_query = f"""
                        DELETE FROM {table_name}
                        WHERE created_on <= %s;
                    """
                    cursor.execute(delete_query, [archival_date])
                    logger.info(f"Deleted {cursor.rowcount} records from {table_name}")
            else:
                logger.info(f"No records to archive for {table_name}.")

        logger.info("Archival task completed successfully.")
    except Exception as e:
        logger.error(f"Archival task failed: {str(e)}")


@shared_task(name='archival_api.services.deletion_service')
def deletion_service():
    try:
        # Get the current date
        now = timezone.now()

        # Loop through each table in the ArchivalConfig that needs records deletion
        from archival_api.models import ArchivalConfig
        configs = ArchivalConfig.objects.all()

        for config in configs:
            table_name = config.table_name
            deletion_period_days = config.deletion_period_days  # Assume you store deletion period in your config

            # Calculate the deletion date (N days ago)
            deletion_date = now - timedelta(days=deletion_period_days)

            # Use transaction.atomic() to handle transactions automatically for database operations
            with transaction.atomic():
                # Fetch records from the archived_db that are older than 'deletion_date'
                cursor = connections['archived_db'].cursor()
                try:
                    # Dynamically fetch column names for the table from the archived_db
                    cursor.execute(f"DESCRIBE archival_api_archived{table_name};")
                    columns = [column[0] for column in cursor.fetchall()]  # column[0] contains column names

                    # Fetch records older than 'deletion_date'
                    query = f"""
                        SELECT * FROM archival_api_archived{table_name} 
                        WHERE created_on <= %s; 
                    """
                    cursor.execute(query, [deletion_date])
                    rows_to_delete = cursor.fetchall()

                finally:
                    cursor.close()  # Close the cursor after fetching data

                if rows_to_delete:
                    logger.info(f"Found {len(rows_to_delete)} records to delete from table {table_name} in archived_db")

                    # Delete records older than 'deletion_date' from archived_db
                    cursor = connections['archived_db'].cursor()
                    try:
                        delete_query = f"""
                            DELETE FROM archival_api_archived{table_name}
                            WHERE created_on <= %s;
                        """
                        cursor.execute(delete_query, [deletion_date])
                        logger.info(f"Deleted {cursor.rowcount} records from {table_name} in archived_db.")
                    finally:
                        cursor.close()  # Close the cursor after the delete operation
                else:
                    logger.info(f"No records to delete for {table_name} in archived_db.")

        logger.info("Deletion task completed successfully.")
    except Exception as e:
        logger.error(f"Deletion task failed: {str(e)}")
