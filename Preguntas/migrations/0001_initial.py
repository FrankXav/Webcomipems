# Generated by Django 4.0.3 on 2022-03-18 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50)),
                ('correctos_m', models.IntegerField(default=0)),
                ('intentos_m', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=500)),
                ('correctos_p', models.IntegerField(default=0)),
                ('intentos_p', models.IntegerField(default=0)),
                ('materia_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preguntas.materias')),
            ],
        ),
        migrations.CreateModel(
            name='opciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=200)),
                ('correcta', models.BooleanField(default=False)),
                ('pregunta_o', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preguntas.preguntas')),
            ],
        ),
    ]