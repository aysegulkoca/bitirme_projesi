from django.shortcuts import render
import nmap

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
                    blank = blank + ' \n port : %s\t\t\tname : %s\t\t\tversion : %s\t\t\türün : %s' % (port, name, version, product)
        forhost = "\n" + host + " ipli cihaz için: " + blank
        result = result + forhost

    response = u"Nmap tarama sonucu: %s\n" % result
    return response

