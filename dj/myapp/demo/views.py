from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    # return HttpResponse("Test")
    template = loader.get_template('test.html')
    return HttpResponse(template.render())
 