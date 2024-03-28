import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection, OperationalError
from django.db.utils import ProgrammingError


class Command(BaseCommand):
    help = 'Clears the database including all data and migrations'

    def add_arguments(self, parser):
        parser.add_argument('database_type', type=str, help='Specify the type of database (sqlite or postgres)')

    def handle(self, *args, **options):
        database_type = options['database_type'].lower()

        if database_type not in ['sqlite', 'postgres']:
            self.stderr.write(self.style.ERROR('Invalid database type. Please specify either "sqlite" or "postgres".'))
            return

        apps = settings.INSTALLED_APPS

        for app in apps:
            migrations_dir = os.path.join(settings.BASE_DIR, app, 'migrations')
            try:
                for file_name in os.listdir(migrations_dir):
                    if file_name != '__init__.py' and not file_name.startswith('__'):
                        os.remove(os.path.join(migrations_dir, file_name))
            except FileNotFoundError:
                pass

        if database_type == 'sqlite':
            try:
                os.remove(os.path.join(settings.BASE_DIR, 'db.sqlite3'))
            except FileNotFoundError:
                pass
        elif database_type == 'postgres':
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
            except OperationalError as e:
                self.stderr.write(self.style.ERROR(f'Failed to clear database: {e}'))
                return

        self.stdout.write(self.style.SUCCESS('Database cleared successfully.'))
