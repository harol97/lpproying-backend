from django.contrib.admin import ModelAdmin as DjangoModelAdmin


class ModelAdmin(DjangoModelAdmin):
    list_per_page = 20
