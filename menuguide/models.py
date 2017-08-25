from django.db import models

# Create your models here.

# ImageField 사용을 위해서는 Pillow 라이브러리가 필요하다. pip install pillow
# ImageFiled는 기본적으로 데이터가 있어야만 하는 필드


## 수정 필요 사항
# Cocktail, SideDish는 Country 항목이 필요없다.
# 상속받은 Class에서 해당 항목을 삭제 또는 없애는 방법? (Null Data 처리?)

class MenuBase(models.Model):
    BEER_KIND = (
        "Lager", "Ale", "Stout", "IPA"
    )
    COUNTRY_LIST = (
        "USA", "Ireland", "Belgium"
    )
    BASE_KIND = (
        "Vodka", "Gin", "Rum", "Whisky"
    )
    WINE_KIND = (
        "Red", "White", "Sparkling"
    )
    WINE_STYLE = (
        "Dry", "Sweet"
    )
    SIDEDISH_KIND = (
        "Pizza", "Salad", "Fried"
    )
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=1, choices=COUNTRY_LIST)
    description = models.TextField()
    Picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100,
        null=True
    )

class DraftBeer(MenuBase):
    kind = models.CharField(max_length=1, choices=BEER_KIND)
    alc = models.IntegerField()

class BottleBeer(MenuBase):
    kind = models.CharField(max_length=1, choices=BEER_KIND)
    alc = models.IntegerField()

class Cocktail(MenuBase):
    base = models.CharField(max_length=30, choices=BASE_KIND)
    ingredients = models.TextField()

class Wine(MenuBase):
    kind = models.CharField(max_length=1, choices=WINE_KIND)
    style = models.CharField(max_length=30, choices=WINE_STYLE)

class SideDish(MenuBase):
    kind = models.CharField(max_length=1, choices=SIDEDISH_KIND)
