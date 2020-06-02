from django.contrib import admin

from foodapp.models import Person, Product, Intake, Meal, ProductPair, ProductToPerson

# Register your models here.

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Intake)
admin.site.register(Meal)
admin.site.register(ProductPair)
admin.site.register(ProductToPerson)
