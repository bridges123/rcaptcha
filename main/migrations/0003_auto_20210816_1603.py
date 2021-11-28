# Generated by Django 3.2.5 on 2021-08-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customer_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='record_delay',
            field=models.FloatField(default=0, verbose_name='Рекорд с задержкой'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='record',
            field=models.FloatField(default=0, verbose_name='Рекорд без задержки'),
        ),
    ]
