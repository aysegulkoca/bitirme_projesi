from django import template
from scannetwork.models import Vulnerability

register = template.Library()


@register.simple_tag
def calculate_cve_score(vulnerabilities):
    score = 0.0
    for vul in vulnerabilities:
        cve = Vulnerability.objects.get(vulnerability=vul)
        score = score + cve.score
    if len(vulnerabilities) != 0:
        score = score/len(vulnerabilities)
    return score