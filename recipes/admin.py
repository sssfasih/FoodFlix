from django.contrib import admin

# Register your models here.

from .models import User,Recipe,Category

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Category)

