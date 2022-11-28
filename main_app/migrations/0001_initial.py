# Generated by Django 4.1.3 on 2022-11-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PopFigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=100)),
                ('franchise', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('feature', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
