import nmap
from django.shortcuts import render

# Create your views here.
from scannetwork.forms import NmapForm


def nmap_view(request):
    form = NmapForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            ip = form.cleaned_data.get('ip')

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
                            blank = blank + ' \n port : %s\tname : %s\tversion : %s' % (port, name, version )
                forhost = "\n" + host + "ipli cihaz için: " + blank
                result = result + forhost

            response = u"Nmap tarama sonucu: %s\n" % result
            return render(request, 'templates/result.html', {'results': response})
        else:
            form = NmapForm
    return render(request, 'templates/home.html', {'form': form})