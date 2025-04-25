from django.shortcuts import render  # Import the render function to render templates
from django.http import HttpResponse  # Import HttpResponse to send HTTP responses
from django.views import View  # Import View class to create class-based views
from .forms import UserInputForm  # Import the form class
from .llm_factory import create_llm
import requests  # Import the requests library to make HTTP requests

# Create your views here.

class UserInputView(View):
    def get(self, request):
        form = UserInputForm()  # Instantiate the form
        return render(request, 'textapp/index.html', {'form': form})  # Render the template with the form

    def post(self, request):
        user_text = request.POST.get('user_text', '')
        # pick provider via querystring, default to OpenAI
        provider = request.GET.get('provider', 'openai')
        model = request.GET.get('model', None)

        try:
            client = create_llm(provider, model)
        except ValueError as e:
            return HttpResponse(f'Error: {e}', status=400)

        try:
            chat_response = client.get_response(user_text)
        except Exception as exc:
            return HttpResponse(
                f'LLM request to {provider} failed: {exc}', 
                status=502
            )

        return HttpResponse(f'{provider} response: {chat_response}')  # Return the ChatGPT response as an HTTP response

def user_input(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text', '')
        convert_to_uppercase = request.POST.get('convert_to_uppercase')

        if convert_to_uppercase:
            user_text = user_text.upper()

        # same factory wiring here:
        provider = request.GET.get('provider', 'openai')
        try:
            client = get_llm_client(provider)
        except ValueError as e:
            return render(
                request, 
                'text_processor/textapp/index.html', 
                {'error': str(e)}
            )

        try:
            chatgpt_response = client.get_response(user_text)
        except Exception as exc:
            return render(
                request,
                'text_processor/textapp/index.html',
                {'error': f'{provider} failure: {exc}'}
            )

        return render(
            request,
            'text_processor/textapp/index.html',
            {
                'processed_text': user_text,
                'chatgpt_response': chatgpt_response,
                'provider': provider
            }
        )

    # GET
    return render(request, 'text_processor/textapp/index.html')
