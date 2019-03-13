import nmap
from django.shortcuts import render

# Create your views here.
from scannetwork.forms import NmapForm


def nmap_view(request):
    form = NmapForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            ip = form.cleaned_data.get('ip')

            nm = nmap.PortScanner()
            nm.scan(ip, '22-443')

            r = ""
            for host in nm.all_hosts():
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        r = r + ' \n port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])

            response = u"Nmap tarama sonucu: %s\n" % r
            return render(request, 'templates/result.html', {'results': response})
        else:
            form = NmapForm
    return render(request, 'templates/home.html', {'form': form})