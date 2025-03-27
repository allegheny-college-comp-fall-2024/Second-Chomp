from django import forms

class UserInputForm(forms.Form):
    user_text = forms.CharField(label='Text', max_length=100)
