# Generated by Django 3.0.7 on 2020-06-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200618_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.TextField(default='-'),
        ),
    ]
