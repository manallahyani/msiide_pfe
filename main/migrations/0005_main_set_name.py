# Generated by Django 3.0.7 on 2020-06-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200610_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='-'),
        ),
    ]
