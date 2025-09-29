import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # --- LLM ---
    llm_provider: str = "openai"
    llm_model: str = "gpt-4o-mini"
    llm_api_key: str

    # --- Database ---
    db_url: str = "sqlite:///./agent.db"

    # --- Search / External APIs ---
    search_api_key: str
    search_engine: str = "tavily"

    # --- Agent Default Settings ---
    default_persona: str = "friendly"
    default_emotion: str = "neutral"

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), ".env")
        env_file_encoding = "utf-8"
