from twilio.rest import Client
from openai import OpenAI
from django.conf import settings
import json


def send_twilio_message(to, message):

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=to,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=message
    )
    print(f"Sent message: {message.sid}")

def call_openai(message_content):

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    messages = [
        {"role": "system", "content": "You are a mission-critical analyst for SMS messages."},
        {"role": "user", "content": f"Analyze the following SMS content: '{message_content}'."},
        {"role": "user", "content": "Identify if the SMS answers the question of 'What and in which quantity is needed where and when'. If the request SMS covers the info, return the info in Expected Output Format and mark 'evaluation' as 'complete'. If some info is missing, mark it in Expected Output Format behind any missing info key as 'missing' for value and 'evaluation' as 'Incomplete'."},
        {"role": "user", "content": "Expected Output Format: {'resource_needed': 'string', 'quantity': 'string', 'location': 'string', 'timeline': 'string', 'evaluation': 'string'}"},
        {"role": "user", "content": "If the SMS is not in ENG language, please return the response in ENG after translating"}
    ]

    try:
        # Send the request to OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )

        # Extract the response
        ai_response_text = response.choices[0].message.content.strip()
        print(f"AI Response: {ai_response_text}")  # Print the AI response for debugging

        # Attempt to parse the response as JSON
        try:
            ai_response_json = json.loads(ai_response_text)
        except json.JSONDecodeError:
            print("Error parsing AI response as JSON.")
            ai_response_json = None

        # Decide if more info is needed
        needs_more_info = ai_response_json is not None and ai_response_json.get("evaluation", "").lower() == "incomplete"

        return {
            'response_text': ai_response_text,
            'response_json': ai_response_json,
            'needs_more_info': needs_more_info
        }

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return {
            'response_text': None,
            'response_json': None,
            'needs_more_info': False
        }


