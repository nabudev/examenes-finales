# Generated by Django 5.0.6 on 2024-05-20 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0003_alter_examen_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='fecha_limite_inscripcion',
            field=models.DateTimeField(),
        ),
    ]
