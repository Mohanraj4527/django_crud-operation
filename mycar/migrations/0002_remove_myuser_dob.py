# Generated by Django 5.1.7 on 2025-04-01 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='Dob',
        ),
    ]
