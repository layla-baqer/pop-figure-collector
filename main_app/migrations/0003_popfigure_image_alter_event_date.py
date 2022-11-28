# Generated by Django 4.1.3 on 2022-11-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='popfigure',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Event Date'),
        ),
    ]
