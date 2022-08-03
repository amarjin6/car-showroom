# Generated by Django 4.0.6 on 2022-08-03 12:40

import core.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_alter_currency_acronym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='acronym',
            field=models.CharField(choices=[('US Dollar', 'USD'), ('Euro', 'EUR'), ('Ruble', 'RUB'), ('Zloty', 'PLN'), ('Hryvnia', 'UAH'), ('Yen', 'JPY'), ('Yuan', 'CNY'), ('Turkish Lira', 'TRY'), ('Lira', 'ITL'), ('Bitcoin', 'BTC')], default=core.enums.Acronym['USD'], max_length=30, unique=True),
        ),
    ]
