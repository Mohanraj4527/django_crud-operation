# Generated by Django 5.1.7 on 2025-03-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Dob', models.DateField()),
                ('Phone', models.BigIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Model', models.CharField(max_length=20)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
