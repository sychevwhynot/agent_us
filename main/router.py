"""Основное приложение принимающее запросы."""

from main.agents import (
    agent_executor,
    agent_type
)
from main.utils import load_yaml


TYPES_TASKS = {
    "install": "instruction_install.yaml",
    "uninstall": "instruction_uninstall.yaml"
}


def router(data):
    """Роутер управляющий агентами."""

    data_desc = data.description
    data_type = agent_type(data_desc)

    if data_type.content not in TYPES_TASKS:
        return {"status": "MISS", "description": "Такой тип обращений не обрабатывается"}

    print (f"Тип обращения: {data_type.content}")
    instruction = TYPES_TASKS[data_type.content]
    instruction_str = load_yaml(instruction)
    response = agent_executor(instruction_str, data)
    content = response.content
    return content
