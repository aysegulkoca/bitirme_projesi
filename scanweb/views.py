from django.shortcuts import render,HttpResponse
from .forms import WebForm
from .models import Scanweb
import requests as req
import re
from bs4 import BeautifulSoup


def scan_web(request):
    if request.method == 'POST':
        form = WebForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            title = form.cleaned_data.get('title')
            # queries = open("scanweb\queries.txt")
            # data = queries.readlines()
            # for i in range(len(data)):
            #     query = data[i]
            #     newUrl = url + query
            #     resp = req.get(newUrl)
            #     source = BeautifulSoup(resp.content,"html")
            #
            #     if source==" ":
            #         o = "SQL Injection zafiyeti barındırıyor olabilir. ÖNERİ vs"
            #         break
            #
            #     sqlinjection = open("scanweb\sqlinjection.txt")
            #     sdata = sqlinjection.readlines()
            #     for i in range(len(sdata)):
            #         finds = source.find(string=re.compile(sdata[i]))
            #         if finds:



        return render(request, 'templates/scanweb/scanweb_detail.html', {'o': o})

    else:

        form = WebForm()

        return render(request, 'templates/scanweb/scanweb.html', {'form': form})

#def sql_injection(request):
#urli al
    #o = url
# taranacak ıp ye istekte bulun
# sayfayı bs4 ile parse et
#sql varlığında dönecek değerler ile karşılaştır.
#sonuç dön
                    # list = req.get(url)
                    # payload = open("scanweb\queries.txt")
                    # data = payload.readlines()
                    # for i in range(len(data)):
                    #     query = data[i]
                    #     newUrl = url + query
                    #     resp = req.get(newUrl)
                    #     content = resp.text
                    #     newList = re.sub('<[^<]+?>', '', content)
                    #     if list == newList:
                    #         continue
                    #     else:
                    #         o = "sql injection zafiyeti vardır!"
                    #         break
#         return render(request, 'templates/scanweb/scanweb_detail.html', {'o': o})
