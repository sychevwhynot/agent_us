"""Настройка LLM-модели."""

import os

from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("API_KEY"),
    model="deepseek/deepseek-chat-v3.1",
    temperature=0.0,
    top_p=0.0,
)
