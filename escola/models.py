from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class Modulos(models.Model):
    nome = models.CharField(max_length=140, null=False, blank=False)
    legenda = models.CharField(max_length=180, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    tag = models.CharField(max_length=80, null=False, blank=False)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return f"Modulos [nome={self.nome}]"

class Cursos(models.Model):
    OPCOES_MODULOS = [
        ("TEOLOGIA", "Teologia"),
        ("PSICOLOGIA", "Psicologia"),
        ("HEBRAICO", "Hebraico"),
    ]
    nome = models.CharField(max_length=140, null=False, blank=False)
    legenda = models.CharField(max_length=180, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    modulo = models.CharField(max_length=140, choices=OPCOES_MODULOS, default='')
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return f"Cursos [nome={self.nome}]"
    
    @property
    def modulo_tag(self):
        return self.modulo.tag

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    alunos = models.ManyToManyField(User, related_name='turmas')

    def __str__(self):
        return f"Turma [nome={self.nome}]"

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turmas = models.ManyToManyField(Turma, related_name='professores')

    def __str__(self):
        return f"Professor [user={self.user.username}]"

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos_do_aluno')
    cursos_adquiridos = models.ManyToManyField(Cursos, related_name='alunos', blank=True)
    boletim = models.CharField(max_length=140, null=False, blank=False)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return f"Aluno [user={self.user.username}]"

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return self.nome

class Faltas(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='faltas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='faltas')
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Faltas [aluno={self.aluno.user.username}, materia={self.materia.nome}, quantidade={self.quantidade}]"

class Diretor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Diretor [user={self.user.username}]"
