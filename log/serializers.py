from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Log
    fields = ('log_id', 'log_date', 'log_user', 'event_name', 'event_payload', 'client_timestamp')