from django.test import TestCase  # Import TestCase to create test cases
from django.urls import reverse  # Import reverse to get URL by name

class UserInputViewTests(TestCase):
    def test_get_request(self):
        """Test GET request to UserInputView"""
        response = self.client.get(reverse('user_input'))  # Send GET request to the view
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, '<form')  # Check if the response contains a form

    def test_post_request(self):
        """Test POST request to UserInputView"""
        response = self.client.post(reverse('user_input'), {'user_text': 'hello'})  # Send POST request with user input
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, 'You entered: hello')  # Check if the response contains the processed input

    def test_post_request_with_uppercase(self):
        """Test POST request to user_input view with convert_to_uppercase"""
        response = self.client.post(reverse('user_input'), {'user_text': 'hello', 'convert_to_uppercase': 'on'})  # Send POST request with user input and convert_to_uppercase
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200
        self.assertContains(response, 'HELLO')  # Check if the response contains the uppercase text
