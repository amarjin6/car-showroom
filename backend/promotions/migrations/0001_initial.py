# Generated by Django 4.0.6 on 2022-08-10 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealer', '0001_initial'),
        ('cars', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('discount', models.IntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_promotion', to='cars.car')),
                ('dealer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealer_promotion', to='dealer.dealer')),
                ('vendor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_promotion', to='users.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]