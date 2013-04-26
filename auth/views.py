# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson

def auth_user(request):
    status = {'status': "failure"}
    try:
        username = request.GET['u']
        password = request.GET['p']

        user = User.objects.get(username=username)
        


        status['status'] = "success"

    except KeyError as e:
        status['message'] = "Missing arguments"
    return HttpResponse(simplejson.dumps({'token':'hi, i\'m your token'}), mimetype="application/json")
    return HttpResponse(simplejson.dumps(status), mimetype="application/json")

def auth_verify(request):
    
    return HttpResponse(simplejson.dumps({'status':True}), mimetype="application/json")
