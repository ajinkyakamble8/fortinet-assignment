from django.apps import AppConfig


class ArchivalApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'archival_api'

    def ready(self):
        import archival_api.services  # Make sure this imports the tasks
