# Generated by Django 2.0.6 on 2018-07-16 03:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('readbook', '0003_auto_20180716_1108'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0019_auto_20180716_1120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReadBookCommnet',
            new_name='ReadBookComment',
        ),
    ]