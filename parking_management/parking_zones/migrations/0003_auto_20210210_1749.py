# Generated by Django 3.1.6 on 2024-02-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_zones', '0002_auto_20210210_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_zone',
            name='vacant_slots',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
