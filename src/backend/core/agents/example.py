from langchain.chat_models import init_chat_model

from langgraph.prebuilt import create_react_agent

from src.backend.utils.settings import SettingsLLM

configLLM = SettingsLLM()

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

llm = init_chat_model(
    model=configLLM.model,
    model_provider=configLLM.model_provider,
    base_url=configLLM.base_url
    )

agent = create_react_agent(
    model=llm,
    tools=[get_weather],
)