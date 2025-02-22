from django.db import models

class ArchiveModel(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    archived_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class ArchivedStudent(ArchiveModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class ArchivedTeacher(ArchiveModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=255)

class ArchivalConfig(models.Model):
    table_name = models.CharField(max_length=255)  # The table to archive
    archival_period_days = models.IntegerField(default=180)  # Archival period in days, default to 6 months
    deletion_period_days = models.IntegerField(default=730)  # deletion period in days, default to 2 years