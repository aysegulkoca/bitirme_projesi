from django.shortcuts import render
import nmap
from .models import Vulnerability, Product, Service, Version


# Create your views here.


def nmapscan(ip):
    try:
        nmapresult = nmap.PortScanner()
        nmapresult.scan(ip, arguments='-sV --script firewall-bypass')

        result = {}
        for host in nmapresult.all_hosts():
            port_dic = {}
            for protocoll in nmapresult[host].all_protocols():
                for port in nmapresult[host][protocoll].keys():
                    if nmapresult[host][protocoll][port]['state'] == "open":
                        name = nmapresult[host][protocoll][port]['name']
                        version = nmapresult[host][protocoll][port]['version']
                        product = nmapresult[host][protocoll][port]['product']
                        vulnerability = searchvulnerability(name, version, product)
                        port_dic.setdefault(port, {'service': name, 'version': version, 'product': product, 'vulnerability': vulnerability})
                        result.setdefault(host, port_dic)

        return result
    except ImportError:
        os.system("pip install python-nmap")


def searchvulnerability(service, version, product):
    version_id = None
    product_id = None
    service_id = None
    try:
        version_id = Version.objects.get(version=version)
        product_id = Product.objects.get(product_name=product)
        service_id = Service.objects.get(service_name=service)
    except Version.DoesNotExist:
        version_id = None
    except Service.DoesNotExist:
        service_id = None
    except Product.DoesNotExist:
        product_id = None

    vulnerability = []
    if version_id is not None and product_id is not None and service_id is not None:
        for data in Vulnerability.objects.filter(product_id=product_id, version_id=version_id, service_id=service_id):
            vulnerability.append(data.vulnerability)
    elif version_id is not None and service_id is not None:
        for data in Vulnerability.objects.filter(version_id=version_id, service_id=service_id):
            vulnerability.append(data.vulnerability)
    else:
        vulnerability = []

    return vulnerability


def cve_detail(request, vulnerability):
    cve = Vulnerability.objects.get(vulnerability=vulnerability)
    return render(request, 'templates/scannetwork/cve_detail.html', {'cve': cve})


