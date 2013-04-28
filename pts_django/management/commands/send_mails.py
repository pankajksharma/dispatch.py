from django.core.management.base import BaseCommand, CommandError

from pts_django.dispatch import send_mails

class Command(BaseCommand):
    help = 'Sends mail to relevent subscribers'

    def handle(self, *args, **kwargs):
        send_mails()