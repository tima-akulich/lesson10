# Generated by Django 2.1 on 2018-11-05 17:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.CharField(max_length=64)),
                ('url', models.URLField(max_length=500)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('traceback', models.TextField()),
            ],
        ),
    ]
