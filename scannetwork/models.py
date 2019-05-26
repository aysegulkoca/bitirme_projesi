from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name="product_service")
    total_vulnerability = models.FloatField(verbose_name="p_total_vulnerability")
    service_id = models.ForeignKey("Service", verbose_name="service_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Service(models.Model):
    service_name = models.CharField(max_length=200, verbose_name="product_name")

    def __str__(self):
        return self.service_name


class Version(models.Model):
    version = models.CharField(max_length=200, verbose_name="version")
    total_vulnerability = models.FloatField(verbose_name="v_total_vulnerability")

    def __str__(self):
        return self.version


class ServiceVersion(models.Model):
    version_id = models.ForeignKey("Version", verbose_name="version_id", on_delete=models.CASCADE)
    service_id = models.ForeignKey("Service", verbose_name="service_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Vulnerability(models.Model):
    vulnerability = models.CharField(max_length=200, verbose_name="vulnerability")
    description = models.TextField(verbose_name="description")
    solution = models.TextField(verbose_name="solution")
    cvss_score_v2 = models.FloatField(verbose_name="cvss_score_v2", null=True, blank=True, default=None)
    cvss_score_v3 = models.FloatField(verbose_name="cvss_score_v3", null=True, blank=True, default=None)
    impact_subscore = models.FloatField(verbose_name="impact_subscore", null=True, blank=True, default=None)
    exploitability_subscore = models.FloatField(verbose_name="exploitability_subscore", null=True, blank=True, default=None)
    risk_score = models.FloatField(verbose_name="risk_score", null=True, blank=True, default=None)
    version_id = models.ForeignKey("Version", verbose_name="version_id", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product", verbose_name="product_id", on_delete=models.CASCADE)
    service_id = models.ForeignKey("Service", verbose_name="service_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.vulnerability
