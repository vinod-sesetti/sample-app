from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    print "***"*20
    print "welcome to app_calendar index"
    print "***"*20
    response = TemplateResponse(request, 'app_calendar/index.html')
    return response
