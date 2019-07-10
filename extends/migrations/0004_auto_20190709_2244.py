# Generated by Django 2.0.6 on 2019-07-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extends', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_paid',
            field=models.CharField(default='F', max_length=10),
        ),
        migrations.AddField(
            model_name='payment',
            name='message',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='payment',
            name='attach',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='payment',
            name='body',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total_fee',
            field=models.IntegerField(default=0),
        ),
    ]
