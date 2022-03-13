from rest_framework import viewsets
from .models import Log
from .serializers import LogSerializer
from rest_framework.response import Response

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = Log.objects.all()
    #     serializer = LogSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request)