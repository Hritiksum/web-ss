#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

#from .models import *


import base64
import os
import urllib.parse as urlparse
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
from selenium import webdriver
#DRIVER = 'chromedriver'

def home(request):
    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url', '')
        import os
        #os.chmod('media/chromedriver.exe', 0o755)
        try:
            os.chmod('media/linux64/chromedriver', 0o755)
            wd = webdriver.Chrome(executable_path=r'media/linux64/chromedriver')
            print("tried linux64")
        except:
            try:
                os.chmod('media/linux32/chromedriver', 0o755)
                wd = webdriver.Chrome(executable_path=r'media/linux32/chromedriver')
                print("tried linux32")
            except:
                try:
                    os.chmod('media/mac64/chromedriver', 0o755)
                    wd = webdriver.Chrome(executable_path=r'media/mac64/chromedriver')
                    print("tried mac64")
                except:
                    os.chmod('media/win/chromedriver.exe', 0o755)
                    wd = webdriver.Chrome(executable_path=r'media/win/chromedriver.exe')
                    print("tried win")
        
        wd.set_window_size(1200, 770)
        wd.get(url)
        wd.save_screenshot('static/my_screenshot.png')
        img_des='static/my_screenshot.png'
        wd.quit()
        return render(request, 'index.html',{'f5':img_des})
    else:
        return render(request, 'index.html')

def error_404_view(request, exception):
    return render(request,'404.html')