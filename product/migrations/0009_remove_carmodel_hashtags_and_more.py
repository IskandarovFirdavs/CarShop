# Generated by Django 5.1.5 on 2025-02-01 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_commentmodel_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='hashtags',
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='hashtags',
        ),
    ]
