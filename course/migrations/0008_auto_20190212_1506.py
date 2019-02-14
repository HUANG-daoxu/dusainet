# Generated by Django 2.0.6 on 2019-02-12 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20181213_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='stacklens', max_length=100, verbose_name='拥有者')),
                ('repo', models.CharField(max_length=500, verbose_name='仓库名')),
                ('title', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(max_length=500, verbose_name='简介')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='github_repo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.GithubRepo'),
        ),
    ]
