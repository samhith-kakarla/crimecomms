# Generated by Django 3.0.5 on 2020-12-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='crime_match',
            field=models.CharField(default='1', max_length=500),
        ),
    ]
