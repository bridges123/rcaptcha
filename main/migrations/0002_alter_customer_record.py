# Generated by Django 3.2.5 on 2021-08-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='record',
            field=models.FloatField(default=0, verbose_name='Рекорд'),
        ),
    ]