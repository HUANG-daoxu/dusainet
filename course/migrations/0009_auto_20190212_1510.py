# Generated by Django 2.0.6 on 2019-02-12 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20190212_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='githubrepo',
            options={'verbose_name_plural': 'Github仓库'},
        ),
        migrations.RemoveField(
            model_name='githubrepo',
            name='title',
        ),
    ]
