
"""Run some command."""

import datetime
import os
from django.core.management.base import BaseCommand
from foodapp.models import Person, Report, Meal, Intake, Product, ProductToPerson, ProductPair, ProductGroup
from random import choice, randint, sample


class Command(BaseCommand):
    """A Django command."""


    def handle(self, *args, **options):
        """A Django command body."""
        person = Person.objects.get(name='klapshov')
        prs = [p for p in ProductToPerson.objects.filter(person=person)]
        #prs = sample(prs, 5)
        # for p in prs:
        #     print(p.product.name)
        part = 3
        prot_lim = None
        prot_th = 135//part
        prot_tgt = None

        kkal_lim = 1800//part
        kkal_th = None
        kkal_tgt = None

        fat_th = 100//part

        fiber_th = 1000//part

        fruits = list(ProductGroup.objects.get(name='Фрукты - клетчатка').product_set.all())
        veggies = list(ProductGroup.objects.get(name='Овощи - клетчатка').product_set.all())
        fibers = fruits+veggies

        while True:
            pp = sample(prs,12//part)
            ppw = [(p, randint(1, 50)*10) for p in pp]
            
            ksum = sum([p[0].product.kkal*p[1]/100 for p in ppw])
            psum = sum([p[0].product.prot*p[1]/100 for p in ppw])
            fsum = sum([p[0].product.fat*p[1]/100 for p in ppw])

            fiber = sum([p[1] for p in ppw if p[0].product in fibers])


            if ksum<kkal_lim and ksum>kkal_lim*0.9 and psum>=prot_th and fsum>=fat_th and fiber>=fiber_th:
                for p in ppw:
                    print(p[0].product.name, p[1])
                break
