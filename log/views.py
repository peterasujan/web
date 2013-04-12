# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson
from log.models import *

@csrf_exempt
def save_log(request):
    status = {'status': "failure"}
    if request.method == 'POST':
        try:
            import pdb;pdb.set_trace()
            subject = request.POST['subject']
            verb = request.POST['verb']
            object = request.POST['object']
            
            status['status'] = "success"
            status['message'] = subject + " " + verb + " " + object

        except KeyError as e:
            status['message'] = "Missing arguments"
    else:            
        status['message'] = "Bad HTTP request type"

    return HttpResponse(simplejson.dumps(status), mimetype="application/json")
