from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_chatgpt_response(prompt_text):
    response = client.ChatCompletions.create(
        model="gpt-4o",  # or another model like "text-davinci-003"
        messages=[
            {
                "role": "system",
                "content": "You are a social media bias detection assistant."
            },
            {
                "role": "assistant",
                "content": "Your goal is to identify potential racial bias in user-submitted content, including overt racism, covert racism, microaggressions, and other nuanced forms of bias."
            },
            {
                "role": "assistant",
                "content": "Provide an analysis of any detected bias, explain why it is problematic, and suggest ways to make the content more inclusive and fair."
            },
            {
                "role": "assistant",
                "content": "If the submitted content contains biased or offensive language, suggest a revised version that conveys the intended message in a more inclusive and respectful way."
            },
            {
                "role": "assistant",
                "content": "Thank you for submitting your content for review. I will analyze it for potential racial bias and provide constructive feedback."
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ]
    )

    return response.choices[0].message.content


