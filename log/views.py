from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
import json
from .models import Log
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.

@csrf_exempt
def create_log(request):
  print(request.body)
  data = json.loads(request.body)

  log_user = data['user']
  event_name = data['eventName']
  event_payload = data['payload']

  new_log = Log(log_user=log_user, event_name=event_name, event_payload=json.dumps(event_payload))

  new_log.save()

  return JsonResponse({'status': 'ok'})

@csrf_exempt
def dump_log(request):
  logs = Log.objects.all()
  res = serialize('json', logs)
  return res