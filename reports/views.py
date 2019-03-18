from django.shortcuts import render
from .models import Report

# Create your views here.


def report_list(request):
    reports = Report.objects.all()
    return render(request, 'templates/reports/report_list.html', {'reports': reports})


def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request, 'templates/reports/report_detail.html', {'report': report})


def report_delete(request, pk):
    reports = Report.objects.all()
    report = Report.objects.get(pk=pk)
    report.delete()
    return render(request, 'templates/reports/report_list.html', {'reports': reports})