from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
class Command(BaseCommand):
    help = 'Create a superuser with a specified password'

    def handle(self, *args, **kwargs):
        username = os.environ.get('USERNAME')
        email = os.environ.get('EMAIL')
        password = os.environ.get('PASSWD')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
