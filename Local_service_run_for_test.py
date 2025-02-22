from archival_api.services import archival_service
from celery.result import AsyncResult

# Call the Celery task
result = archival_service.delay()  # This will return the AsyncResult object

# Wait for the task to complete or check its status periodically
while not result.ready():  # Checks if the task is complete
    print(f"Task Status: {result.status}")
    time.sleep(1)  # Wait for 1 second before checking again

# Once done, print the result
if result.status == 'SUCCESS':
    print(f"Task Completed! Result: {result.result}")
elif result.status == 'FAILURE':
    print(f"Task Failed with error: {result.result}")



########################################################################

from archival_api.services import deletion_service
from celery.result import AsyncResult

# Call the Celery task
result = deletion_service.delay()  # This will return the AsyncResult object

# Wait for the task to complete or check its status periodically
while not result.ready():  # Checks if the task is complete
    print(f"Task Status: {result.status}")
    time.sleep(1)  # Wait for 1 second before checking again

# Once done, print the result
if result.status == 'SUCCESS':
    print(f"Task Completed! Result: {result.result}")
elif result.status == 'FAILURE':
    print(f"Task Failed with error: {result.result}")
