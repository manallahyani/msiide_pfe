# Generated by Django 3.0.7 on 2020-06-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200618_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='picname',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='main',
            name='picurl',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='tel',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=40),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=40),
        ),
    ]