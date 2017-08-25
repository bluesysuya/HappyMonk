from django.db import models

# Create your models here.

# ImageField 사용을 위해서는 Pillow 라이브러리가 필요하다. pip install pillow
# ImageFiled는 기본적으로 데이터가 있어야만 하는 필드


## 수정 필요 사항
# 1. 맥주 분류 Choice 항목 추가
# 2. 국가 Choice 항목 추가

class MenuBase(models.Model):
    BEER_KIND = (
        "Lager", "Ale", "Stout", "IPA"
    )
    COUNTRY_LIST = (
        "USA", "United Kingdom", "Ireland", "Belgium"
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

class DraftBeer(MenuBase):
    pass

class BottleBeer(MenuBase):
    pass

class Cocktail(MenuBase):
    base = models.CharField(max_length=30)
    ingredients = models.TextField()

class Wine(MenuBase):
    WINE_KIND = (
        "Red", "White", "Sparkling"
    )
    WINE_STYLE = (
        "Dry", "Sweet"
    )
    kind = models.CharField(max_length=1, choices=WINE_KIND)
    style = models.CharField(max_length=30)

class SideDish(MenuBase):
    SIDEDISH_KIND = (
        "Pizza", "Salad", "Fried"
    )
    kind = models.CharField(max_length=1, choices=SIDEDISH_KIND)
