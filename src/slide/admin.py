from django.contrib import admin

from utils.django.model_admin import ModelAdmin

from .models import Slide


@admin.register(Slide)
class SlideAdmin(ModelAdmin): ...
