from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import Shop
import uuid
from datetime import time
import requests


@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return render(request, 'index.html', {'range': range(int(data['times'])), 'text': data['text']})


@csrf_exempt
def add_shop(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for i in range(data['times']):
            Shop.objects.create(name=uuid.uuid4(), city=uuid.uuid4(), street=uuid.uuid4(
            ), street_number=7, open_at=time(hour=7, minute=0), close_at=time(hour=21, minute=0)).save()
        return HttpResponse(status=201)


@csrf_exempt
def clear_shops_table(request):
    Shop.objects.all().delete()
    return HttpResponse(status=200)


def external_api_call(request):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=3096472&APPID=39d3a15f5bdcab980c739b931b9c2863')
    return HttpResponse(r.text)
