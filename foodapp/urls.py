from django.urls import path
from foodapp import views

urlpatterns = [
    path('', views.week_list, name='week_list'),
    path('search', views.search, name='search'),
    path('ac', views.ac, name='ac'),
]