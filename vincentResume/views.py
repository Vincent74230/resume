from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('vincentResume/index.html')
    return HttpResponse(template.render({}, request))

def cv(request):
    template = loader.get_template('vincentResume/cv.html')
    return HttpResponse(template.render({}, request))
