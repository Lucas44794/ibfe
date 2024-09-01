from django.urls import path, include
from escola.views import modulos, logout, curso
from . import views


urlpatterns = [
    path('modulos', modulos, name= 'modulos'),
    path('logout', logout, name='logout'),
    path('curso/<int:curso_id>/', views.curso, name='curso'),
    
]
