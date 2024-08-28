from django.urls import path
from home.views import index, contato, login


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    
]
