from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully'))