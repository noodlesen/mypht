
"""step2"""

import datetime
import os
import json
from django.core.management.base import BaseCommand
from foodapp.models import Person, Report, Meal, Intake, Product, ProductPair, ProductToPerson
from operator import attrgetter
from collections import Counter


class Command(BaseCommand):
    """A Django command."""


    def handle(self, *args, **options):
        """A Django command body."""

        ProductToPerson.objects.all().delete()

        person = Person.objects.get(name='klapshov')
        intakes = Intake.objects.filter(person=person)

        for i in intakes:
            try:
                p2p = ProductToPerson.objects.get(person=person, product=i.product)
            except ProductToPerson.DoesNotExist:
                p2p = ProductToPerson(person=person, product=i.product)

            p2p.intakes_count+=1

            print(p2p)

            weights = json.loads(p2p.weights)
            weights.append(i.weight)
            p2p.weights = json.dumps(weights)

            if i.weight<p2p.w_min or p2p.w_min==0:
                p2p.w_min = i.weight



            if i.weight>p2p.w_max:
                p2p.w_max = i.weight


            typical = [(k,v) for k,v in Counter(weights).items() if v>1]
            p2p.w_typ = json.dumps(typical)

            p2p.w_avg = int(sum(weights)/len(weights))



            p2p.save()

