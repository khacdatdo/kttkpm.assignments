import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from ...models import Country


class Command(BaseCommand):
    help = "Extracting Country data to JSON format"

    def handle(self, *args, **options):
        country_data = Country.objects.all()
        for country in country_data:
            data = {
                "model": "Country",
                "country_name": country.country_name,
                "local_currency": country.local_currency,
                "added_on": country.added_on
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")
