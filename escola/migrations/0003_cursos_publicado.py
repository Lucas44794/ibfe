# Generated by Django 5.1 on 2024-08-31 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
