from django.urls import path
from .views import receive_sms, get_sms_data, get_sms_val_dump

app_name = 'core'

urlpatterns = [
    path('receive-sms/', receive_sms, name='receive_sms'),
    path('sms-data/', get_sms_data, name='get_sms_data'),
    path('sms-val-dump/', get_sms_val_dump, name='get_sms_val_dump'),
]

# /api/ patern in root urls - here need them clean w/o api/