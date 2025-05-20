from django.db import models


class Service(models.Model):
    title: models.CharField = models.CharField()
    subtitle = models.CharField()
    short_description = models.CharField()
    description = models.CharField()
    image_url = models.URLField()

    def __str__(self):
        return self.title.__str__()


class Feature(models.Model):
    value = models.CharField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Image(models.Model):
    image_url = models.URLField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)