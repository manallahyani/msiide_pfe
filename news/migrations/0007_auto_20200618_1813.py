# Generated by Django 3.0.7 on 2020-06-18 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200615_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='views',
            new_name='show',
        ),
    ]
