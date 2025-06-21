from django.db import models


class Slide(models.Model):
    title = models.CharField(null=True, blank=True)
    image_path = models.ImageField(upload_to="page_images/slide/")
    description = models.CharField(null=True, blank=True)
    text = models.CharField(null=True, blank=True)
    href = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.image_path.__str__()
