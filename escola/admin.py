from django.contrib import admin
from escola.models import Modulos, Cursos, Turma, Professor, Aluno, Diretor

class ListandoModulos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "tag")
    list_display_links = ("id", "nome")
    list_per_page = 20

class ListandoCursos(admin.ModelAdmin):
    list_display = ("id", "nome", "curso", "tag")
    list_display_links = ("id", "nome")
    list_per_page = 20

class ListandoTurmas(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao")
    list_display_links = ("id", "nome")
    list_per_page = 20

class ListandoProfessores(admin.ModelAdmin):
    list_display = ("id", "user", "get_turmas")
    list_display_links = ("id", "user")
    list_per_page = 20

    def get_turmas(self, obj):
        return ", ".join([turma.nome for turma in obj.turmas.all()])
    get_turmas.short_description = 'Turmas'

class ListandoAlunos(admin.ModelAdmin):
    list_display = ("id", "user", "turma")
    list_display_links = ("id", "user")
    list_per_page = 20

class ListandoDiretores(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")
    list_per_page = 20

admin.site.register(Modulos, ListandoModulos)
admin.site.register(Cursos, ListandoCursos)
admin.site.register(Turma, ListandoTurmas)
admin.site.register(Professor, ListandoProfessores)
admin.site.register(Aluno, ListandoAlunos)
admin.site.register(Diretor, ListandoDiretores)
