# core/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SMSData
from .utils import send_twilio_message

@csrf_exempt  # Disable CSRF for this view, as it will be called by Twilio's servers
def receive_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('From')
        message_content = request.POST.get('Body')

        # Save the incoming SMS data
        sms_data = SMSData.objects.create(
            phone_number=phone_number,
            message_content=message_content,
            status='pending'
        )

        # Simulate processing the message content
        # ai_response = call_openai(message_content)  # Commented out OpenAI-related logic for now

        # For now, let's assume we always need more information
        follow_up_question = "What is the specific information you need?"

        # Send a follow-up SMS using Twilio
        send_twilio_message(phone_number, follow_up_question)

        return JsonResponse({'status': 'processed', 'message': 'Data processed successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
