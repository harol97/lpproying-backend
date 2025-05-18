from django.contrib import admin

from utils.django.model_admin import ModelAdmin

from .models import Service, ServiceFeature


class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    inlines = (ServiceFeatureInline,)
