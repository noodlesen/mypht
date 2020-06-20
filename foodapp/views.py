from django.shortcuts import render
from foodapp.models import Person, Meal
from datetime import datetime, timedelta, date
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product
# Create your views here.
def week_list(request):
    person = Person.objects.get(name='klapshov')
    today = datetime.today()
    dow = today.weekday()
    monday = today - timedelta(days=dow+7)
    from_date = monday
    from_date = date(2020, 6, 1)
    meals = Meal.objects.filter(date__gte=from_date)
    res = []
    for m in meals:
        resm = {}
        resm['name'] = m.date.strftime("%d/%m/%y") + " - " + str(m.meal_number)
        resm['intakes'] = m.intake_set.all()
        res.append(resm)


    print('monday', monday)
    return render(request, 'foodapp/week_list.html', {"res": res})

def search(request):
    return render(request, 'foodapp/search.html', {})

#@require_POST
def ac(request):
    names = [obj.name for obj in Product.objects.all()]
    return JsonResponse(names, safe=False)