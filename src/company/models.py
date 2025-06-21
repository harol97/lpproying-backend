from django.db import models


class Company(models.Model):
    name = models.CharField()
    phone = models.CharField()
    email = models.CharField()
    address = models.CharField()
    businessHours = models.CharField()
    logo_path = models.ImageField(upload_to="page_images/company/")

    def __str__(self):
        return self.name.__str__()


class ContactRequest(models.Model):
    fullname = models.CharField(verbose_name="Nombres Completos")
    email = models.EmailField(verbose_name="correo")
    phone = models.CharField(max_length=20, verbose_name="telefono")
    company = models.CharField(verbose_name="empresa")
    message = models.CharField(verbose_name="message")
    subject = models.TextField(verbose_name="asunto")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="fecha de creación"
    )
