# Generated by Django 5.1 on 2024-09-01 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0012_remove_cursos_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='curso',
        ),
    ]
