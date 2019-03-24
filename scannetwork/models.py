from django.db import models

# Create your models here.


class Service(models.Model):
    service_name = models.CharField(max_length=200, verbose_name="product_name")
    product = models.CharField(max_length=200, verbose_name="product_service")

    def __str__(self):
        return self.service_name


class Version(models.Model):
    version = models.CharField(max_length=200, verbose_name="version")
    service = models.ForeignKey("Service", verbose_name="service_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.version


class Vulnerability(models.Model):
    vulnerability = models.CharField(max_length=200, verbose_name="vulnerability")
    description = models.TextField(verbose_name="description")
    solution = models.TextField(verbose_name="solution")
    code = models.TextField(verbose_name="code")
    version = models.ForeignKey("Version", verbose_name="version_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.vulnerability