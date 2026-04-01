from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission


class Command(BaseCommand):
    help = 'Assign can_create_application permission to a user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found!'))

        perm = Permission.objects.get(codename='can_create_application')
        user.user_permissions.add(perm)

        self.stdout.write(self.style.SUCCESS(f'Create application permission granted to {username}'))
