# Generated by Django 3.2.5 on 2021-08-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_customer_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avg',
            field=models.FloatField(default=0, verbose_name='Среднее время'),
        ),
    ]
