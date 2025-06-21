from django.db import models


class Service(models.Model):
    title: models.CharField = models.CharField()
    subtitle = models.CharField()
    short_description = models.CharField()
    description = models.CharField()
    image_path = models.ImageField(upload_to="page_images/service/")

    def __str__(self):
        return self.title.__str__()


class Feature(models.Model):
    value = models.CharField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Image(models.Model):
    image_path = models.ImageField(upload_to="page_images/service/")
    description = models.CharField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

