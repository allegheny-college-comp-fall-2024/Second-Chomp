from .llm_clients import OpenAIClient, AnthropicClient, CohereClient

# registry of LLM clients being used 

CLIENTS = {
    "openai": OpenAIClient,
    "anthropic": AnthropicClient,
    "cohere": CohereClient,
}

def create_llm(provider: str, model:str = None):
    """
    Factory function to get the appropriate LLM client based on the client name.
    """
    try:
        client_cls = CLIENTS[provider.lower()]
    except KeyError:
            raise ValueError(f"Unknown LLM provider: '{provider}'.")
    return client_cls()
