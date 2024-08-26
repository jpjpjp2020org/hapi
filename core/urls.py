from django.urls import path
from .views import receive_sms

app_name = 'core'

urlpatterns = [
    path('receive-sms/', receive_sms, name='receive_sms'),
]
