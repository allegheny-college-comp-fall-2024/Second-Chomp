from django.urls import path  # Import the path function to define URL patterns
from . import views  # Import views from the current package
from .views import UserInputView  # Import the UserInputView class-based view
#from .views import DeepSeekView  # Import the DeepSeekView class-based view

urlpatterns = [
    path('user-input/', UserInputView.as_view(), name='user_input'),  # URL pattern for the class-based view
    path('user_input/', views.user_input, name='user_input'),  # URL pattern for the function-based view
    # path('deepseek/', DeepSeekView.as_view(), name='deepseek'),  # URL pattern for the deepseek API
    # path('deepseek-ai/', views.deepseek_ai_view, name='deepseek_ai'),  # URL pattern for the DeepSeek AI view
]
