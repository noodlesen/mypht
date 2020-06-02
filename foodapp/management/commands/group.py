
"""step4"""

import datetime
import os
from django.core.management.base import BaseCommand
from foodapp.models import Person, Report, Meal, Intake, Product, ProductPair, ProductGroup
from operator import attrgetter


class Command(BaseCommand):
    """A Django command."""


    def handle(self, *args, **options):
        """A Django command body."""

        ProductGroup.objects.all().delete()

        products = Product.objects.all()

        #ФРУКТЫ
        print('- фрукты')
        pg = ProductGroup(name='Фрукты - клетчатка')
        pg.save()

        keys = ['яблоко', 'груша', 'банан', 'виноград','клубника']

        for p in products:
            for k in keys:
                if k in p.name.lower():
                    p.groups.add(pg)
                    print(p.name)

        #ОВОЩИ
        print ('- овощи')
        pg = ProductGroup(name='Овощи - клетчатка')
        pg.save()

        keys = ['огурец', 'огурцы', 'томат', 'помидор', 'капуста', 'салат айсберг', 'морковь', 'цукини', 'авокадо', 'лук', 'горошек', 'шампиньоны', 'кабачки']
        stops = ['кетчуп', 'соус']

        for p in products:
            have_key = False
            have_stops = False
            for k in keys:
                if k in p.name.lower():
                    have_key = True

            if have_key:
                for s in stops:
                    if s in p.name.lower():
                        have_stops = True

                if not have_stops:
                    p.groups.add(pg)
                    print(p.name)

