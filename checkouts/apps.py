from django.apps import AppConfig


class CheckoutsConfig(AppConfig):
    name = 'checkouts'

    def ready(self):
        import checkouts.signals