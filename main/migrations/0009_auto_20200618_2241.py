# Generated by Django 3.0.7 on 2020-06-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200618_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='picname',
            field=models.TextField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='picurl',
            field=models.TextField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='tel',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
