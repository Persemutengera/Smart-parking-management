# Generated by Django 3.1.6 on 2024-02-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_zones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_zone',
            name='vacant_slots',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
