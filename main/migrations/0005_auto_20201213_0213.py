# Generated by Django 3.0.5 on 2020-12-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201212_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='crime_match',
            field=models.IntegerField(default=0),
        ),
    ]
