from abc import ABC, abstractmethod
import os
from django.conf import settings
from openai import OpenAI
import anthropic
import cohere


class BaseLLMClient(ABC):
    """Base class for LLM Clients."""

    @abstractmethod
    def get_response(self, prompt_text: str) -> str:
        """
        Send `prompt_text` to the LLM and return the assistant's reply.
        """
        pass


class OpenAIClient(BaseLLMClient):
    def __init__(self, model_name: str = None):
        api_key = os.getenv("OPEN_AI", settings.OPENAI_API_KEY)
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o"

    def get_response(self, prompt_text: str) -> str:
        response = self.client.chat.completions.create(
            model= self.model,
            messages=[
                {"role": "system", "content": "You are a social media bias detection assistant."},
                {"role": "assistant", "content": (
                    "Your goal is to identify potential racial bias in user-submitted "
                    "content, including overt racism, covert racism, microaggressions, "
                    "and other nuanced forms of bias."
                )},
                {"role": "assistant", "content": (
                    "Provide an analysis of any detected bias, explain why it is "
                    "problematic, and suggest ways to make the content more inclusive and fair."
                )},
                {"role": "assistant", "content": (
                    "If the submitted content contains biased or offensive language, "
                    "suggest a revised version that conveys the intended message in a "
                    "more inclusive and respectful way."
                )},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message.content


class AnthropicClient(BaseLLMClient):
    def __init__(self, model_name: str = None):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY", settings.ANTHROPIC_API_KEY))
        self.model = "claude-3-opus-20240229"

    def get_response(self, prompt_text: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {"role": "user", "content": (
                    "You are a social media bias detection assistant. "
                    "Your goal is to identify potential racial bias in user-submitted content, including overt racism, covert racism, microaggressions, "
                    "and nuanced bias. Analyze the input, explain any issues, and suggest more inclusive alternatives. "
                ) + f"Content: {prompt_text}"}
            ]
        )
        return response.content[0].text


class CohereClient(BaseLLMClient):
    def __init__(self):
        self.client = cohere.Client(
            os.getenv("COHERE_API_KEY", settings.COHERE_API_KEY))
        self.model = "command-r-plus"

    def get_response(self, prompt_text: str) -> str:
        response = self.client.chat(
            model=self.model,
            message=(
                "You are a social media bias detection assistant. "
                "Your task is to review the submitted text for racial bias, overt or subtle. "
                "Offer an explanation and suggest a respectful rewrite if needed. "
                f"Content: {prompt_text}"
            ),
            temperature=0.5,
        )
        return response.text
