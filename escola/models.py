from django.db import models
from django.contrib.auth.models import User

class Modulos(models.Model):
    nome = models.CharField(max_length=140, null=False, blank=False)
    legenda = models.CharField(max_length=180, null=False, blank=False)
    foto = models.CharField(max_length=140, null=False, blank=False)
    tag = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return f"Modulos [nome={self.nome}]"

class Cursos(models.Model):
    curso = models.CharField(max_length=100, null=False, blank=False)
    nome = models.CharField(max_length=140, null=False, blank=False)
    legenda = models.CharField(max_length=180, null=False, blank=False)
    foto = models.CharField(max_length=140, null=False, blank=False)
    tag = models.CharField(max_length=80, null=False, blank=False)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return f"Cursos [nome={self.nome}]"

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"Turma [nome={self.nome}]"

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turmas = models.ManyToManyField(Turma, related_name='professores')

    def __str__(self):
        return f"Professor [user={self.user.username}]"

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return f"Aluno [user={self.user.username}]"

class Diretor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Diretor [user={self.user.username}]"
