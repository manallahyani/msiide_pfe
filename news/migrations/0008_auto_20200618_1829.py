# Generated by Django 3.0.7 on 2020-06-18 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200618_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='show',
            new_name='views',
        ),
    ]
