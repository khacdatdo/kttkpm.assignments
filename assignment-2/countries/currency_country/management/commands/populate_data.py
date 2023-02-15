import json
import sys
import logging
from dateutil import parser
from django.core.management.base import BaseCommand
from ...models import Country

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Populating Country data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating Country Model
            if data["model"] == "Country":
                country = Country(
                    country_name=data["country_name"],
                    local_currency=data["local_currency"],
                    added_on=parser.parse(data["added_on"])
                )
                country.save()
                logger.debug("Country populated:{}".format(
                    country.country_name))
