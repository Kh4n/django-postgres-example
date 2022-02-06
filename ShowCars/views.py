from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from ShowCars.models import Car, car_qs_to_json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.template import loader


@api_view(['GET', 'POST'])
def get_cars(request):
    return JsonResponse(car_qs_to_json(Car.objects.all()))


def view_cars(request):
    template = loader.get_template("all_cars.html")
    return HttpResponse(template.render({}, request))
