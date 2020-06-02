
"""step3"""

from django.core.management.base import BaseCommand
from foodapp.models import Person, Meal, ProductPair, ProductToPerson


class Command(BaseCommand):
    """A Django command."""

    def handle(self, *args, **options):
        """A Django command body."""

        ProductPair.objects.all().delete()
        person = Person.objects.get(name='klapshov')
        meals = Meal.objects.filter(person=person)
        for m in meals:
            products = [i.product for i in m.intake_set.all()]
            print(products)
            pairs = []
            for n in range(0, len(products)-1):
                for nn in range(n+1, len(products)):
                    if n != nn:
                        pairs.append([products[n], products[nn]])
            print(pairs)
            print(len(products), len(pairs))

            # REWRITE!!!!!!!!
            for p in pairs:
                try:
                    pp = ProductPair.objects.get(product1=p[0], product2=p[1])
                except ProductPair.DoesNotExist:
                    pp = ProductPair()
                    pp.product1 = p[0]
                    pp.product2 = p[1]
                    pp.count = 1
                    p2p = ProductToPerson.objects.get(
                        person=person, product=p[0]
                    )
                    pp.ratio = round(pp.count/p2p.intakes_count*100)
                    pp.save()
                else:
                    pp.count += 1
                    p2p = ProductToPerson.objects.get(
                        person=person,
                        product=p[0]
                    )
                    pp.ratio = round(pp.count/p2p.intakes_count*100)
                    pp.save()

            for p in pairs:
                p.reverse()
                try:
                    pp = ProductPair.objects.get(product1=p[0], product2=p[1])
                except ProductPair.DoesNotExist:
                    pp = ProductPair()
                    pp.product1 = p[0]
                    pp.product2 = p[1]
                    pp.count = 1
                    p2p = ProductToPerson.objects.get(
                        person=person,
                        product=p[0]
                    )
                    pp.ratio = round(pp.count/p2p.intakes_count*100)
                    pp.save()
                else:
                    pp.count += 1
                    p2p = ProductToPerson.objects.get(
                        person=person,
                        product=p[0]
                    )
                    pp.ratio = round(pp.count/p2p.intakes_count*100)
                    pp.save()
