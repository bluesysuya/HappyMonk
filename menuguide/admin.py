from django.contrib import admin
from .models import DraftBeer, BottleBeer, Cocktail, Wine, SideDish

# Register your models here.

@admin.register(DraftBeer, BottleBeer, Cocktail, Wine, SideDish)
class MenuGuideAdmin(admin.ModelAdmin):
    pass
