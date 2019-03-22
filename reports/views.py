from django.shortcuts import render, redirect
from scannetwork.views import nmapscan
from .models import Report
from .forms import ReportForm

# Create your views here.


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