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
            log_items = request.POST['logs']
            for log_item in log_items:
                subject = User.objects.get(username=log_item['subject'])
                verb = Verb.objects.get(verb=log_item['verb'])
                object = log_item['object']
                aLog = ActivityLog(subject=subject, verb=verb, object=object)
                aLog.save()
            
            status['status'] = "success"

        except KeyError as e:
            status['message'] = "Missing arguments"
    else:            
        status['message'] = "Bad HTTP request type"

    return HttpResponse(simplejson.dumps(status), mimetype="application/json")
