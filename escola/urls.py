from django.urls import path, include
from escola.views import modulos, logout, curso


urlpatterns = [
    path('modulos', modulos, name= 'modulos'),
    path('logout', logout, name='logout'),
    path('curso', curso, name='curso'),
    
]
