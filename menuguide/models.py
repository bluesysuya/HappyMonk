from django.db import models

# Create your models here.

# ImageField 사용을 위해서는 Pillow 라이브러리가 필요하다. pip install pillow
# ImageFiled는 기본적으로 데이터가 있어야만 하는 필드


## 수정 필요 사항
# Cocktail, SideDish는 Country 항목이 필요없다.
# 상속받은 Class에서 해당 항목을 삭제 또는 없애는 방법? (Null Data 처리?)

# class MenuBase(models.Model):
#     COUNTRY_LIST = (
#         ('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')
#     )
#     name = models.CharField(max_length=30)
#     country = models.CharField(max_length=1, choices=COUNTRY_LIST)
#     description = models.TextField()
#     Picture = models.ImageField(
#         upload_to=None, height_field=None, width_field=None, max_length=100,
#         null=True
#     )

class DraftBeer(models.Model):
    BEER_KIND = (
        ('Lager', 'LAGER'), ('Ale', 'ALE'), ('Stout', 'STOUT')
    )
    COUNTRY_LIST = (
        ('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')
    )
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=1, choices=BEER_KIND)
    country = models.CharField(max_length=1, choices=COUNTRY_LIST)
    alc = models.IntegerField()
    description = models.TextField()
    Picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,
        null=True
    )

class BottleBeer(models.Model):
    BEER_KIND = (
        ('Lager', 'LAGER'), ('Ale', 'ALE'), ('Stout', 'STOUT')
    )
    COUNTRY_LIST = (
        ('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')
    )
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=1, choices=BEER_KIND)
    alc = models.IntegerField()
    country = models.CharField(max_length=1, choices=COUNTRY_LIST)
    description = models.TextField()
    Picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,
        null=True
    )

class Cocktail(models.Model):
    BASE_KIND = (
        ('Vodka', 'VODKA'), ('Gin', 'GIN'), ('Rum', 'RUM')
    )
    name = models.CharField(max_length=30)
    base = models.CharField(max_length=30, choices=BASE_KIND)
    alc = models.IntegerField()
    ingredients = models.TextField()
    description = models.TextField()
    Picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,
        null=True
    )

class Wine(models.Model):
    WINE_KIND = (
        ('Red', 'RED'), ('White', 'WHITE'), ('Sparkling', 'SPLARKLING')
    )
    WINE_STYLE = (
        ('Dry', 'DRY'), ('Sweet', 'SWEET')
    )
    COUNTRY_LIST = (
        ('USA', 'USA'), ('Ireland', 'IRELAND'), ('Belgium', 'BELGIUM')
    )
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=1, choices=WINE_KIND)
    country = models.CharField(max_length=1, choices=COUNTRY_LIST)
    style = models.CharField(max_length=30, choices=WINE_STYLE)
    alc = models.IntegerField()
    description = models.TextField()
    Picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,
        null=True
    )

class SideDish(models.Model):
    SIDEDISH_KIND = (
        ('Pizza', 'PIZZA'), ('Salad', 'SALAD')
    )
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=1, choices=SIDEDISH_KIND)
    description = models.TextField()
    Picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,
        null=True
    )
