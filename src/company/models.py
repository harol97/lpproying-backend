from django.db import models


class Company(models.Model):
    name = models.CharField()
    phone = models.CharField()
    email = models.CharField()
    businessHours = models.CharField()
    logo = models.URLField()

    def __str__(self):
        return self.name.__str__()
