import json
from django.shortcuts import render, redirect
from scannetwork.views import nmapscan
from django.core.paginator import Paginator
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
            report.content = json.dumps(response)
            report.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'templates/reports/home.html', {'form': form})


def report_list(request):
    report_list = Report.objects.all()
    paginator = Paginator(report_list, 5)  # her sayfada 5 rapor göster

    page = request.GET.get('page')
    reports = paginator.get_page(page)
    return render(request, 'templates/reports/report_list.html', {'reports': reports})


def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    title = report.title
    content = json.loads(report.content)
    date = report.created_date
    return render(request, 'templates/reports/report_detail_list.html', {'title': title, 'content': content, 'date': date})


def report_delete(request, pk):
    reports = Report.objects.all()
    report = Report.objects.get(pk=pk)
    report.delete()
    return render(request, 'templates/reports/report_list.html', {'reports': reports})