from django.core.management.base import BaseCommand
from core.utils import call_openai

class Command(BaseCommand):
    help = 'Test OpenAI API integration'

    def handle(self, *args, **kwargs):
        test_message = "Need 5 generators at 123 Main St, ASAP."
        test_message = "Need 5 generators ASAP."
        response = call_openai(test_message)
        print("\nTEST: OpenAI API response:")
        print(response)
