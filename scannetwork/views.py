from django.shortcuts import render
import nmap
from .models import Vulnerability, Product, Service, Version

# Create your views here.


def nmapscan(ip):
    nmapresult = nmap.PortScanner()
    nmapresult.scan(ip, arguments='-sV --script firewall-bypass')

    result = ""
    for host in nmapresult.all_hosts():
        blank = ""
        prototocols = nmapresult[host].all_protocols()
        for protocoll in prototocols:
            ports = nmapresult[host][protocoll].keys()
            for port in ports:
                if nmapresult[host][protocoll][port]['state'] == "open":
                    name = nmapresult[host][protocoll][port]['name']
                    version = nmapresult[host][protocoll][port]['version']
                    product = nmapresult[host][protocoll][port]['product']
                    vulnerability = searchvulnerability(name, version, product)
                    blank = blank + ' \n port : %s\t\t\tname : %s\t\t\tversion : %s\t\t\türün : %s\nzafiyetleri: \n%s' % (port, name, version, product, vulnerability)
        forhost = "\n" + host + " ipli cihaz için: " + blank
        result = result + forhost

    response = u"Nmap tarama sonucu: %s\n" % result
    return response


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

    vulnerability = ""
    if version_id is not None and product_id is not None and service_id is not None:
        for data in Vulnerability.objects.filter(product_id=product_id, version_id=version_id, service_id=service_id):
            vulnerability = vulnerability + '\n' + data.vulnerability
    elif version_id is not None and service_id is not None:
        for data in Vulnerability.objects.filter(version_id=version_id, service_id=service_id):
            vulnerability = vulnerability + '\n' + data.vulnerability
    else:
        vulnerability = ""

    return vulnerability

