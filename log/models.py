from django.db import models

# Create your models here.
class Log(models.Model):
    """
    Log model
    """
    # Fields
    log_id = models.AutoField(primary_key=True)
    log_date = models.DateTimeField(auto_now_add=True)
    log_user = models.TextField(max_length = 100)
    event_name = models.TextField(max_length=100)
    event_payload = models.TextField(max_length=10000, blank = True)
    client_timestamp = models.DateTimeField()

    # Methods
    def __str__(self):
        return '%s - %s' % (self.log_user, self.event_name)