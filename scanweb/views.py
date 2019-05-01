from django.shortcuts import render,HttpResponse
from .forms import WebForm
from .models import Scanweb
import requests as req
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import cgi

def scan_web(request):
    if request.method == 'POST':
        form = WebForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            title = form.cleaned_data.get('title')
            sqlInj = sql_injection(url)
            xssVuln = xss(url)
        return render(request, 'templates/scanweb/scanweb_detail.html', {'sqlInj': sqlInj, 'xssVuln':xssVuln})
    else:
        form = WebForm()
        return render(request, 'templates/scanweb/scanweb.html', {'form': form})


def sql_injection(url):
    newUrl = ''
    total = 0

    queries = open("scanweb\queries.txt")
    data = queries.readlines()

    for i in range(len(data)):
        query = data[i]
        newUrl = url + query
        resp = req.get(newUrl)
        source = BeautifulSoup(resp.content, 'html.parser')

        if source == " ":
            total += 1

        sqlinjection = open("scanweb\sqlinjection.txt")
        errors = sqlinjection.readlines()
        for j in range(len(errors)):
            finds = source.find(string=re.compile(errors[j]))
            if finds != None:
                total += 1

    if total == 0:
        output = "SQL Injection zafiyeti barındırmıyor!"
    else:
        output = "SQL Injection zafiyeti barındırıyor olabilir. url:" + newUrl

    return output

def xss(url):
    resp = req.get(url)
    soup = BeautifulSoup(resp.content,'html.parser')
    fields = {}

    for input in soup.findAll('input'):
        if input['type'] in ('text', 'hidden', 'password', 'submit', 'image'):

            value = '<script>alert("XSS")</script>'

            if 'value' in input:
                value = input['value']
            fields[input['name']] = value

    for textarea in soup.findAll('textarea'):
        fields[textarea['name']] = textarea.string or ''

    a = requests.post(url,fields)
    return a