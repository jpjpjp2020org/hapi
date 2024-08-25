from django.urls import path
from .views import receive_sms

app_name = 'core'

urlpatterns = [
    path('api/receive-sms/', receive_sms, name='receive_sms'),
]
