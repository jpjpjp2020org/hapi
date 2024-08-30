from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SMSData, SMSValDump
from .utils import call_openai, send_twilio_message

@csrf_exempt  # Disabling CSRF for this view, as it will be called by Twilio's servers
def receive_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('From')
        message_content = request.POST.get('Body')

        # log the incoming SMS data for debugging
        # print(f"RSMS: Received SMS from {phone_number}: {message_content}")
        print(f"RSMS: Received SMS from <redacted>: {message_content}")

        # trigger the OpenAI function with the SMS content
        ai_response = call_openai(message_content)

        if ai_response['response_json'] and not ai_response['needs_more_info']:
            # save the complete response in the main SMSData model
            SMSData.objects.create(
                phone_number=phone_number,  # store the real phone number - aggregation later
                message_content=message_content,
                resource_needed=ai_response['response_json'].get('resource_needed', ''),
                quantity=ai_response['response_json'].get('quantity', ''),
                location=ai_response['response_json'].get('location', ''),
                timeline=ai_response['response_json'].get('timeline', ''),
                evaluation=ai_response['response_json'].get('evaluation', 'incomplete')
            )

            # send a confirmation SMS
            send_twilio_message(phone_number, "Info received!")

        else:
            # save the raw/incomplete message in SMSValDump model
            SMSValDump.objects.create(
                phone_number=phone_number,  # reply to the actual phone number from Twilio's webhook
                message_content=message_content
            )

            # if incomplete, trigger a follow-up SMS asking for more details - initially unified | later can trigger per missing data
            send_twilio_message(phone_number, "Provide more info concisely: what, quantity, location, and when?")

        return JsonResponse({'status': 'processed', 'message': 'Data processed successfully'})

    # log if an invalid request method is received
    print("Invalid request method received.")
    return JsonResponse({'error': 'Invalid request method'}, status=400)
