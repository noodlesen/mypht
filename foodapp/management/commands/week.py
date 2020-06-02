
"""Run some command."""

import datetime
import os
from django.core.management.base import BaseCommand
from foodapp.models import Person, Report, Meal, Intake, Product, ProductToPerson, ProductPair
from random import choice, randint, sample
from datetime import date


class Command(BaseCommand):
    """A Django command."""


    def handle(self, *args, **options):
        """A Django command body."""
        person = Person.objects.get(name='klapshov')
        from_date = date(2020, 5, 25)
        meals = Meal.objects.filter(date__gte=from_date)
        for m in meals:
            print(m)
            print('...')
            for i in m.intake_set.all():
                print(i)
            print()