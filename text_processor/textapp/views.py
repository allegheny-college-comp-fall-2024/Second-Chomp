from django.shortcuts import render  # Import the render function to render templates
from django.http import HttpResponse  # Import HttpResponse to send HTTP responses
from django.views import View  # Import View class to create class-based views
from .forms import UserInputForm  # Import the form class
from .openai_service import get_chatgpt_response  # Import the function to get ChatGPT response
import requests  # Import the requests library to make HTTP requests

# Create your views here.

class UserInputView(View):
    def get(self, request):
        form = UserInputForm()  # Instantiate the form
        return render(request, 'textapp/index.html', {'form': form})  # Render the template with the form

    def post(self, request):
        user_text = request.POST.get('user_text')  # Get the user input from the POST request
        chatgpt_response = get_chatgpt_response(user_text)  # Get the ChatGPT response
        return HttpResponse(f'ChatGPT response: {chatgpt_response}')  # Return the ChatGPT response as an HTTP response

def user_input(request):
    if request.method == 'POST':  # Check if the request method is POST
        user_text = request.POST.get('user_text')  # Get the user input from the POST request
        convert_to_uppercase = request.POST.get('convert_to_uppercase')  # Check if the user wants to convert text to uppercase
        
        if convert_to_uppercase:  # If the checkbox is checked
            user_text = user_text.upper()  # Convert the text to uppercase
        
        chatgpt_response = get_chatgpt_response(user_text)  # Get the ChatGPT response
        return render(request, 'text_processor/textapp/index.html', {'processed_text': user_text, 'chatgpt_response': chatgpt_response})  # Render the template with the processed text and ChatGPT response
    return render(request, 'text_processor/textapp/index.html')  # Render the template without any processed text if the request method is not POST

