from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name="product_name")
    product_service = models.CharField(max_length=200, verbose_name="product_service")


class Version(models.Model):
    version = models.CharField(max_length=200, verbose_name="version")
    product = models.ForeignKey("Product", verbose_name="product_id", on_delete=models.CASCADE)


class Vulnerability(models.Model):
    vulnerability = models.CharField(max_length=200, verbose_name="vulnerability")
    description = models.TextField(verbose_name="description")
    solution = models.TextField(verbose_name="solution")
    code = models.TextField(verbose_name="code")
    version = models.ForeignKey("Version", verbose_name="version_id", on_delete=models.CASCADE)