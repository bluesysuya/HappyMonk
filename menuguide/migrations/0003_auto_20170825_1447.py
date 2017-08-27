# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-25 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuguide', '0002_draftbeer_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(choices=[('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')], max_length=1)),
                ('description', models.TextField()),
                ('Picture', models.ImageField(null=True, upload_to=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='bottlebeer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='bottlebeer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bottlebeer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bottlebeer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='alc',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='id',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='name',
        ),
        migrations.RemoveField(
            model_name='draftbeer',
            name='Picture',
        ),
        migrations.RemoveField(
            model_name='draftbeer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='draftbeer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='draftbeer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='draftbeer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='sidedish',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sidedish',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sidedish',
            name='name',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='alc',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='country',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='description',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='id',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='name',
        ),
        migrations.AlterField(
            model_name='bottlebeer',
            name='kind',
            field=models.CharField(choices=[('Lager', 'LAGER'), ('Ale', 'ALE'), ('Stout', 'STOUT')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='base',
            field=models.CharField(choices=[('Vodka', 'VODKA'), ('Gin', 'GIN'), ('Rum', 'RUM')], max_length=30),
        ),
        migrations.AlterField(
            model_name='draftbeer',
            name='kind',
            field=models.CharField(choices=[('Lager', 'LAGER'), ('Ale', 'ALE'), ('Stout', 'STOUT')], max_length=1),
        ),
        migrations.AlterField(
            model_name='sidedish',
            name='kind',
            field=models.CharField(choices=[('Pizza', 'PIZZA'), ('Salad', 'SALAD')], max_length=1),
        ),
        migrations.AlterField(
            model_name='wine',
            name='kind',
            field=models.CharField(choices=[('Red', 'RED'), ('White', 'WHITE'), ('Sparkling', 'SPLARKLING')], max_length=1),
        ),
        migrations.AlterField(
            model_name='wine',
            name='style',
            field=models.CharField(choices=[('Dry', 'DRY'), ('Sweet', 'SWEET')], max_length=30),
        ),
        migrations.AddField(
            model_name='bottlebeer',
            name='menubase_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menuguide.MenuBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='menubase_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menuguide.MenuBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='draftbeer',
            name='menubase_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menuguide.MenuBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sidedish',
            name='menubase_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menuguide.MenuBase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='menubase_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='menuguide.MenuBase'),
            preserve_default=False,
        ),
    ]
