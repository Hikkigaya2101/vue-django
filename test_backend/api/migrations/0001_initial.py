# Generated by Django 4.2.14 on 2024-12-09 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип подразделения')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.unit', verbose_name='Родитель')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.unittype', verbose_name='Тип подразделения')),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('data_birthday', models.DateField(verbose_name='День рождения')),
                ('data_workday', models.DateField(verbose_name='День выхода на работу')),
                ('consumer_avatar', models.ImageField(upload_to='uploads')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.unit', verbose_name='Подразделение')),
            ],
        ),
    ]
