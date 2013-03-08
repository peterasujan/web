# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def save_log(request):
    return HttpResponse("<h1>Thank you.</h1> Your log has been received and is being processed by /dev/null.")
