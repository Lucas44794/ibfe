# Generated by Django 5.1 on 2024-08-31 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_alter_cursos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulos',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]
