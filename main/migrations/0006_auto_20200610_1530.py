# Generated by Django 3.0.7 on 2020-06-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tel',
            field=models.TextField(default='-'),
        ),
    ]
