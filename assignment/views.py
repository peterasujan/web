# Create your views here.
from assignment.models import Assignment
from django.http import HttpResponse
from django.utils import simplejson as json

def assignment_list(request):
    assigns = []
    for assignment in Assignment.objects.all():
        assign = [assignment.name, assignment.url, str(assignment.date)]
        assigns.append(assign)

    return HttpResponse(json.dumps(assigns), mimetype="application/json")





