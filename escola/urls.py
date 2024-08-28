from django.urls import path, include
from escola.views import modulos


urlpatterns = [
    path('modulos', modulos, name= 'modulos'),
    
]
