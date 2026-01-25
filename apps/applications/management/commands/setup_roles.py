from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create user roles and assign permissions'
    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='Admin')
        create_permission = Permission.objects.get(codename='can_create_application')
        admin_group.permissions.add(create_permission)
        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))
