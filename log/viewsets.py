from rest_framework import viewsets
from .models import Log
from .serializers import LogSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import csv
from django.http import HttpResponse

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = Log.objects.all()
    #     serializer = LogSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request)

    @action(detail=False, methods=['get'])
    def export_logs(self, request):
        queryset = Log.objects.all()

        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename'
        writer = csv.writer(response)
        writer.writerow(['log_id', 'log_date', 'log_user', 'event_name', 'event_payload', 'client_timestamp'])
        for log in queryset:
            writer.writerow([log.log_id, log.log_date, log.log_user, log.event_name, log.event_payload, log.client_timestamp])

        return response
