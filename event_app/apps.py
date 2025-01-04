from django.apps import AppConfig


class EventAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_app'

    def ready(self):
        import event_app.signals
