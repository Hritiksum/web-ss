#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

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
DRIVER = 'chromedriver'
def home(request):
    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url', '')
        wd = webdriver.Chrome(executable_path=r'media/chromedriver.exe')
        wd.set_window_size(1200, 770)
        wd.get(url)
        wd.save_screenshot('static/my_screenshot.png')
        img_des='static/my_screenshot.png'
        wd.quit()
        return render(request, 'index.html',{'f5':img_des})


