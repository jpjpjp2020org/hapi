from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SMSData
# from .utils import send_twilio_message  # - not needed for initial test

@csrf_exempt  # Disabling CSRF for this view, as it will be called by Twilio's servers
def receive_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('From')
        message_content = request.POST.get('Body')

        # log the incoming SMS data for debugging
        print(f"Received SMS from {phone_number}: {message_content}")

        # save the incoming SMS data to the database
        sms_data = SMSData.objects.create(
            phone_number=phone_number,
            message_content=message_content,
            status='pending'
        )

        # log that the data has been saved
        print(f"SMS data saved: {sms_data}")

        # reply loop should handle logic in a moe abstarcted way, not hardcoded like below:
        # follow_up_question = "some follow up question?"

        # reply:
        # send_twilio_message(phone_number, "Conf of reeiving.")

        return JsonResponse({'status': 'processed', 'message': 'Data processed successfully'})

    # Log if an invalid request method is received
    print("Invalid request method received.")
    return JsonResponse({'error': 'Invalid request method'}, status=400)
