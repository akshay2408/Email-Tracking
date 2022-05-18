from django.urls import path
from .views import eventAPI

urlpatterns = [
    path('event', eventAPI),  # create, replied and bounced msg
]
