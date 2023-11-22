# Generated by Django 4.1.13 on 2023-11-20 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medico',
            fields=[
                ('ID_Medico', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('ID_Paciente', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Fecha_Nacimiento', models.DateTimeField()),
                ('Sexo', models.CharField(max_length=20)),
                ('Altura', models.FloatField()),
                ('Medico_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hospital.medico')),
            ],
        ),
    ]