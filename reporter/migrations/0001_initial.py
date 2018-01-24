# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_name', models.CharField(blank=True, max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('article_reported', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'reporter_name',
            },
        ),
    ]
