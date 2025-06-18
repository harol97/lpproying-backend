from django.contrib import admin

from utils.django.model_admin import ModelAdmin

from .models import Service, Feature, Image


class ServiceFeatureInline(admin.TabularInline):
    model = Feature

class ServiceImageInline(admin.StackedInline):
    model= Image


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    inlines = (ServiceFeatureInline, ServiceImageInline)
