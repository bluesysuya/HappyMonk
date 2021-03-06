# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-25 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuguide', '0003_auto_20170825_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottlebeer',
            name='menubase_ptr',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='menubase_ptr',
        ),
        migrations.RemoveField(
            model_name='draftbeer',
            name='menubase_ptr',
        ),
        migrations.RemoveField(
            model_name='sidedish',
            name='menubase_ptr',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='menubase_ptr',
        ),
        migrations.AddField(
            model_name='bottlebeer',
            name='Picture',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='bottlebeer',
            name='country',
            field=models.CharField(choices=[('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')], default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bottlebeer',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bottlebeer',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bottlebeer',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='Picture',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='alc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='draftbeer',
            name='Picture',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='draftbeer',
            name='country',
            field=models.CharField(choices=[('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')], default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='draftbeer',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='draftbeer',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='draftbeer',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sidedish',
            name='Picture',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='sidedish',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sidedish',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sidedish',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='Picture',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='wine',
            name='alc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='country',
            field=models.CharField(choices=[('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')], default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MenuBase',
        ),
    ]
