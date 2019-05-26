from django import template
from scannetwork.models import Vulnerability, Version, Product

register = template.Library()


@register.simple_tag
def calculate_cve_risk_score(vulnerabilities):
    for vul in vulnerabilities:
        cve = Vulnerability.objects.get(vulnerability=vul)
        cve.risk_score = cve.exploitability_subscore * cve.impact_subscore
        cve.save()

    return cve.risk_score


def counter(vul_list):
    medium_risk = 0
    high_risk = 0
    critical_risk = 0

    for vul in vul_list:
        cve = Vulnerability.objects.get(vulnerability=vul)

        if 30.0 < cve.risk_score <= 50.0:
            medium_risk += 1
        elif 50.0 < cve.risk_score <= 80.0:
            high_risk += 1
        elif 80.0 < cve.risk_score <= 100.0:
            critical_risk += 1

    content = [medium_risk, high_risk, critical_risk]
    return content


@register.simple_tag
def write(content_values):
    port_content_list = []
    vul_list = []
    for ports in content_values:
        for port_content in ports.values():
            return port_content
