
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
        meals = Meal.objects.all()
        for m in meals:
            kkal = 0
            prot = 0
            fat = 0
            for i in m.intake_set.all():
                kkal += i.product.kkal * i.weight / 100
                prot += i.product.prot * i.weight / 100
                fat += i.product.fat * i.weight / 100
            if kkal<=450 and prot>=34 :
                print('got it')
            elif kkal<=600 and prot>=45 :
                print('got it')

