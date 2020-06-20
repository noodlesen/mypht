from datetime import timedelta
import os
from django.core.management.base import BaseCommand
from foodapp.models import Person, Meal, Intake, Product


class Command(BaseCommand):
    """A Django command."""

    FROM_FILES = False # Check from files or from meal objects
    def handle(self, *args, **options):
        """A Django command body."""
        person = Person.objects.get(name='klapshov')
        meals = Meal.objects.filter(person=person)
        dates = sorted(list(set([m.date for m in meals])))
        skipped = []
        cday = dates[0]
        while cday<=dates[-1]:
            if cday not in dates:
                skipped.append(cday)
            cday += timedelta(days=1)

        print(f"From {dates[0]} to {dates[-1]}")
        print (skipped)