# from django.urls import path

# from . import views

# urlpatterns = [
#   path('create', views.create_log, name='create_log'),
#   path('dump', views.dump_log, name='dump_log'),
# ]

from . import viewsets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'log', viewsets.LogViewSet)

urlpatterns = router.urls
