import logging

from django.core.management.base import BaseCommand

from apps.contacts.services.generate_contacts import generate_contacts
from apps.contacts.models import Contact


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            help="How many contacts do you wont to generate?",
            type=int,
            default=10
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        logger = logging.getLogger("django")

        queryset = Contact.objects.all()

        logger.info(f"Current amount of contacts beafor: {queryset.count()}")

        for contact in generate_contacts(amount=amount, is_mark_as_autogenerated=True):
            contact.save()
        logger.info(f"Current amount of contacts after: {queryset.count()}")
        print()