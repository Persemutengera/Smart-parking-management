# Generated by Django 3.1.6 on 2024-02-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_zones', '0006_reservation_checked_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='ticket_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
