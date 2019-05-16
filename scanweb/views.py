from django.shortcuts import render,HttpResponse
from .forms import WebForm
from .models import Scanweb
import requests as req
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def scan_web(request):
    if request.method == 'POST':
        form = WebForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            title = form.cleaned_data.get('title')
            try:
                sqlInj = sql_injection(url)
                xssVuln = xss(url)
                bs4(url)
                return render(request, 'templates/scanweb/scanweb_detail.html', {
                    'url': url,
                    'title':title,
                    'sqlInj': sqlInj,
                    'xssVuln':xssVuln
                })
            except ImportError:
                os.system("pip install requests re beautifulsoup4")
    else:
        form = WebForm()
        return render(request, 'templates/scanweb/scanweb.html', {'form': form})

def sql_injection(url):
    newUrl = ''
    total = 0
    dic = bs4(url)
    queries = open("scanweb\queries.txt")
    data = queries.readlines()
    for i in range(len(data)):
        query = data[i]
        newUrl = url + query
        resp = req.get(newUrl)
        source = BeautifulSoup(resp.content, 'html.parser')
        newDic = bs4(newUrl)
        if dic==newDic:
            continue
        else:
            total += 1

        if source == " ":
            total += 1

        sqlinjection = open("scanweb\sqlinjection.txt")
        errors = sqlinjection.readlines()
        for j in range(len(errors)):
            finds = source.find(string=re.compile(errors[j]))
            if finds != None:
                total += 1

    if total == 0:
        output = "barındırmıyor."
    else:
        output = "BARINDIRIYOR!"

    return output

def xss(url):
    xss = 0
    payload = open("scanweb/payload.txt",encoding="utf8")

    value = payload.readlines()
    resp = req.get(url)
    soup = BeautifulSoup(resp.content,'html.parser')

    # Web Sayfalarındaki doldurulan alanalarda XSS denemesi
    fields = {}
    for input in soup.findAll('input'):
        if input['type'] in ('text', 'hidden', 'password', 'image'):
            for i in range(len(value)):
                fields[input['name']] = value[i]
                requests = req.post(url, fields)
                soup2 = BeautifulSoup(requests.content, 'html.parser')
                if value in soup2 :
                    xss += 1
    #Url üzerinden XSS denemesi
    for j in range(len(value)):
        val = value[j]
        xssUrl = url + val
        response = req.get(xssUrl)
        soup3 = BeautifulSoup(response.content,'html.parser')
        if val in soup3:
            xss += 1
    if xss == 0:
        xssOutput = "barındırmıyor"
    else:
        xssOutput = "BARINDIRIYOR!"
    return xssOutput

def bs4(url):
    dic = {}
    resp = req.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    dic =  soup.find_all("td")

    return dic