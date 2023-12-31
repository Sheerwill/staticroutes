# Generated by Django 4.2.5 on 2023-09-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField()),
                ('Booking_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]
