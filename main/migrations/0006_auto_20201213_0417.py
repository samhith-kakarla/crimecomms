# Generated by Django 3.0.5 on 2020-12-13 09:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201213_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='coordinates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2),
        ),
    ]