from django.urls import path, include
from escola.views import modulos, logout


urlpatterns = [
    path('modulos', modulos, name= 'modulos'),
    path('logout', logout, name='logout'),
    
]
