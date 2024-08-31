from django.contrib import admin
from escola.models import Modulos, Cursos

class ListandoModulos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "tag")
    list_display_links = ("id", "nome")
    list_per_page = 20

class ListandoCursos(admin.ModelAdmin):
    list_display = ("id", "nome", "curso", "tag")
    list_display_links = ("id", "nome")
    list_per_page = 20

admin.site.register(Modulos, ListandoModulos)
admin.site.register(Cursos, ListandoCursos)

