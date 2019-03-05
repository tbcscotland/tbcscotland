# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tbc', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('lookingFor', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='Projects_images')),
                ('timeline', models.CharField(max_length=128)),
                ('keywords', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbc.Profile')),
            ],
        ),
    ]
