import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def handle(self, *args, **options):
        User = get_user_model()
        print(os.environ.get("ENV"))
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
                                          email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
                                          password=os.environ.get('DJANGO_SUPERUSER_PASSWORD'))