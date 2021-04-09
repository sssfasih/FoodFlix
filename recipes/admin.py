from django.contrib import admin

# Register your models here.

from .models import User,Recipe,Category,RecipeImage

admin.site.register(User)

admin.site.register(Category)

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ RecipeImageInline, ]

admin.site.register(Recipe, PropertyAdmin)
