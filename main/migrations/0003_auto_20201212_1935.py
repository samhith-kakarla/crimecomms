# Generated by Django 3.0.5 on 2020-12-13 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_signal_crime_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime',
            name='city',
        ),
        migrations.RemoveField(
            model_name='signal',
            name='coordinates',
        ),
    ]