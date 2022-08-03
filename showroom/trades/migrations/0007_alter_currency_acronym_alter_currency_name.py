# Generated by Django 4.0.6 on 2022-08-03 12:48

import core.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0006_alter_currency_acronym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='acronym',
            field=models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('RUB', 'Ruble'), ('PLN', 'Zloty'), ('UAH', 'Hryvnia'), ('JPY', 'Yen'), ('CNY', 'Yuan'), ('TRY', 'Turkish Lira'), ('ITL', 'Lira'), ('BTC', 'Bitcoin')], default=core.enums.Acronym['USD'], max_length=3),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('RUB', 'Ruble'), ('PLN', 'Zloty'), ('UAH', 'Hryvnia'), ('JPY', 'Yen'), ('CNY', 'Yuan'), ('TRY', 'Turkish Lira'), ('ITL', 'Lira'), ('BTC', 'Bitcoin')], default='US Dollar', max_length=30),
        ),
    ]
