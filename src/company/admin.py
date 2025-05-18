from django.contrib import admin

from utils.django.model_admin import ModelAdmin

from .models import Company


@admin.register(Company)
class CompanyAdmin(ModelAdmin): ...
