# Generated by Django 5.1 on 2024-09-01 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0011_cursos_modulos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='tag',
        ),
    ]
