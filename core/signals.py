from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import SMSData, SMSValDump
import requests
import json

# push data to an external endpoint
def push_data_to_client(data, endpoint):

    headers = {'Content-Type': 'application/json'}

    print(f"PDTC: Sending payload to {endpoint}: {data}")

    try:
        response = requests.post(endpoint, json=data, timeout=5, verify=False)
        if response.status_code == 200:
            print(f"PDTC: Successfully pushed data to {endpoint}")
        else:
            print(f"PDTC: Failed to push data to {endpoint}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"PDTC: Error pushing data: {e}")

# django Signal handler for SMSData
@receiver(post_save, sender=SMSData)
def push_sms_data_to_client(sender, instance, created, **kwargs):
    if created and getattr(settings, 'ENABLE_REALTIME_PUSH', False):  # check if push is enabled - , False is fallback default  to keep dormant - EDIT IN SETTINGS NOT IN HERE TO TURN ON.
        # data to push
        data = {
            "phone_number": instance.phone_number,
            "message_content": instance.message_content,
            "resource_needed": instance.resource_needed,
            "quantity": instance.quantity,
            "location": instance.location,
            "timeline": instance.timeline,
            "evaluation": instance.evaluation,
            "created_at": instance.created_at.isoformat(),
        }
        # set the endpoint of the main client
        client_endpoint = getattr(settings, 'MAIN_CLIENT_ENDPOINT_SMS_DATA', None)
        if client_endpoint:
            push_data_to_client(data, client_endpoint)

# django Signal handler for SMSValDump
@receiver(post_save, sender=SMSValDump)
def push_sms_val_dump_to_client(sender, instance, created, **kwargs):
    if created and getattr(settings, 'ENABLE_REALTIME_PUSH', False):  # check if push is enabled - , False is fallback default  to keep dormant - EDIT IN SETTINGS NOT IN HERE TO TURN ON.
        # data to push
        data = {
            "phone_number": instance.phone_number,
            "message_content": instance.message_content,
            "created_at": instance.created_at.isoformat(),
        }
        # set the endpoint of the main client
        client_endpoint = getattr(settings, 'MAIN_CLIENT_ENDPOINT_SMS_VAL_DUMP', None)
        if client_endpoint:
            push_data_to_client(data, client_endpoint)