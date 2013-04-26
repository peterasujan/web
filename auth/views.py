# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson

def auth_user(request):
    return HttpResponse(simplejson.dumps({'token':'hi, i\'m your token'}), mimetype="application/json")

def auth_verify(request):
    
    return HttpResponse(simplejson.dumps({'status':True}), mimetype="application/json")
