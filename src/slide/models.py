from django.db import models


class Slide(models.Model):
    image_url = models.URLField()
    text = models.CharField(null=True, blank=True)
    href = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.image_url.__str__()
