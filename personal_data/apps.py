from django.apps import AppConfig


class PersonalDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal_data'

    def ready(self):
        import personal_data.signals
