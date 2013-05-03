# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response

def process_mvle(request):
    status = {'status': 'failure'}
    if request.method == POST:

        return render_to_response('mvle/single-mc.html', {'data': request.body})

    else:
        status['message'] = "Bad HTTP request type: Use POST instead"
    return HttpResponse(simplejson.dumps(status), mimetype="application/json")
