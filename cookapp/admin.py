from django.contrib import admin
from .models import RecipeModel, CathegoryModel


admin.site.register(RecipeModel)
admin.site.register(CathegoryModel)