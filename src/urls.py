from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('get/<int:id>',views.get, name='get'),
]
