# Generated by Django 5.1.4 on 2025-01-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_car_commentmodel_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
