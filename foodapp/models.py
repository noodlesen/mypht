from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)

class ProductGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    def __str__(self):
        gs = '(%s)' % '/'.join([g.name for g in self.groups.all()])
        return('%s %r, %r, %r, %r %s' % (self.name, self.kkal, self.prot, self.fat, self.carb, gs))
    name = models.CharField(max_length=255)
    kkal = models.FloatField(null=True)
    prot = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    nfat = models.FloatField(null=True)
    carb = models.FloatField(null=True)
    fiber = models.FloatField(null=True)
    sugar = models.FloatField(null=True)
    nat = models.FloatField(null=True)
    holes = models.FloatField(null=True)
    kali = models.FloatField(null=True)
    source = models.CharField(max_length=50, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    is_meta = models.BooleanField(default=False)

    groups = models.ManyToManyField(ProductGroup)

    # # meta product equivalent
    # meta_product = models.ForeignKey(Product, null=True) 



class Person(models.Model):
    def __str__(self):
        return(self.name)
    name = models.CharField(null=True, max_length=255)

class Preference(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Report(models.Model):
    filename = models.CharField(null=True, max_length=255)
    text = models.TextField(null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Meal(models.Model):
    def __str__(self):
        return('%s %s %r' %(self.person.name, self.meal_number, self.date))
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    meal_number = models.IntegerField(null=True)
    date = models.DateField(null=True)

class Intake(models.Model):
    #Кал ( ккал),Жир( г),Н/жир( г),Углев( г),Клетч( г),Сахар( г),Белк( г),Натри( мг),Холес( мг),Калий( мг)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)

    def __str__(self):
        return '%s %d' % (self.product.name, self.weight)

class ProductPair(models.Model):
    def __str__(self):
        return(self.product1.name[:30]+'/'+self.product2.name[:30]+' '+str(self.count))
    product1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product1')
    product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product2')
    count = models.IntegerField(null=True)
    ratio = models.IntegerField(null=True)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class RecipePart(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField(null=True)

class ProductToPerson(models.Model):
    def __str__(self):
        return('%s %s %r' % (self.person.name, self.product.name, self.weights))
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    intakes_count = models.IntegerField(default=0)
    weights = models.TextField(default='[]')  #json
    w_min = models.IntegerField(default=0)
    w_max = models.IntegerField(default=0)
    w_avg = models.IntegerField(default=0)
    w_typ = models.TextField(default='[]')  #json
    is_fav = models.BooleanField(default=False)

class ProductToMeta(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product')
    meta_product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='meta_product')








