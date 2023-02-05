from django.shortcuts import render
from .models import Car
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache


# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL' ,DEFAULT_TIMEOUT)


def get_car(cr = None):
    if cr:
        crr = Car.objects.filter(name__contains = cr)
    else:
        crr = Car.objects.all() 
    return crr 


def index(request):
    cr = request.GET.get('car')
    if cache.get(cr):
        print('Cache')
        car = cache.get(cr)
    else:
        if cr:
            print('Database')
            car = get_car(cr)
            cache.set(cr, car)
        else:
            car = get_car()
    context = {
        'cars': car,
    }
    return render(request, 'index.html', context)

def get(request, id):
    if cache.get(id):
        print('Cache')
        car = cache.get(id)
    else:
        print('Database')
        car = Car.objects.filter(id = id)
        carr = cache.set(id, car)
    context = {
        'car' : car
    }
    return render(request, 'single.html', context)
