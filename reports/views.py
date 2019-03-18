from django.shortcuts import render, redirect
import nmap
from .models import Report
from .forms import ReportForm

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
                    blank = blank + ' \n port : %s\tname : %s\tversion : %s' % (port, name, version)
        forhost = "\n" + host + "ipli cihaz için: " + blank
        result = result + forhost

    response = u"Nmap tarama sonucu: %s\n" % result
    return response


def report_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        report = form.save(commit=False)
        if form.is_valid():

            title = form.cleaned_data.get('title')
            ip = form.cleaned_data.get('ip')

            response = nmapscan(ip)

            report.ip = ip
            report.title = title
            report.text = response
            report.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'templates/reports/home.html', {'form': form})


def report_list(request):
    reports = Report.objects.all()
    return render(request, 'templates/reports/report_list.html', {'reports': reports})


def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request, 'templates/reports/report_detail_list.html', {'report': report})


def report_delete(request, pk):
    reports = Report.objects.all()
    report = Report.objects.get(pk=pk)
    report.delete()
    return render(request, 'templates/reports/report_list.html', {'reports': reports})