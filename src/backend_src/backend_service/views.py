from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
from backend_service.settings import FRONT_DIR

def show_frontend(request):
    return render(request, FRONT_DIR+'/'+'index.html')