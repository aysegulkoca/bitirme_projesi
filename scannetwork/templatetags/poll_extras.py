from django import template
from scannetwork.models import Vulnerability, Version, Product

register = template.Library()


@register.simple_tag
def calculate_cve_risk_score(vulnerabilities):

    for vul in vulnerabilities:
        cve = Vulnerability.objects.get(vulnerability=vul)
        risk = 0.0
        version = None
        product = None
        try:
            version = Version.objects.get(id=cve.version_id_id)
            product = Product.objects.get(id=cve.product_id_id)
        except Version.DoesNotExist:
            version = None
        except Product.DoesNotExist:
            product = None
        if version is not None and product is not None:
            probability = 100 / version.total_vulnerability
            risk = probability * cve.cvss_score
        cve.risk_score = risk
        cve.save()

        result = average(vulnerabilities)
        if result < 30.0:
            return "Çok Düşük"
        elif 30.0 <= result < 50.0:
            return "Düşük"
        elif 50.0 <= result < 70.0:
            return "Ortalama"
        elif 70.0 <= result < 90.0:
            return "Yüksek"
        else:
            return "Kritik"


def average(vulnerabilities):
    score = 0.0
    for vul in vulnerabilities:
        cve = Vulnerability.objects.get(vulnerability=vul)
        score = score + cve.risk_score
    if len(vulnerabilities) != 0:
        score = score/len(vulnerabilities)
    return score
