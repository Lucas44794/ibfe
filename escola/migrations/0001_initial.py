# Generated by Django 5.1 on 2024-08-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
                ('legenda', models.CharField(max_length=180)),
                ('foto', models.CharField(max_length=140)),
                ('tag', models.CharField(max_length=80)),
            ],
        ),
    ]
