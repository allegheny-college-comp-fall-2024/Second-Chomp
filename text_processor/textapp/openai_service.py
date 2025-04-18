# lcsfinder/textapp/views.py  (or wherever your view helper lives)

import os
from django.conf import settings
from openai import OpenAI

# Instantiate a client once, using whatever key source you prefer
API_KEY = os.getenv("OPEN_AI", settings.OPENAI_API_KEY)
client = OpenAI(api_key=API_KEY)


def get_chatgpt_response(prompt_text: str) -> str:
    """
    Send `prompt_text` to the LLM and return the assistant's reply.
    Uses the new OpenAI v1.x python interface.
    """
    response = client.chat.completions.create(
        model="gpt-4o",  # or another deployed model
        messages=[
            {
                "role": "system",
                "content": "You are a social media bias detection assistant."
            },
            {
                "role": "assistant",
                "content": (
                    "Your goal is to identify potential racial bias in user-submitted "
                    "content, including overt racism, covert racism, microaggressions, "
                    "and other nuanced forms of bias."
                )
            },
            {
                "role": "assistant",
                "content": (
                    "Provide an analysis of any detected bias, explain why it is "
                    "problematic, and suggest ways to make the content more inclusive "
                    "and fair."
                )
            },
            {
                "role": "assistant",
                "content": (
                    "If the submitted content contains biased or offensive language, "
                    "suggest a revised version that conveys the intended message in a "
                    "more inclusive and respectful way."
                )
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ]
    )

    # Extract the assistant’s reply
    return response.choices[0].message.content
