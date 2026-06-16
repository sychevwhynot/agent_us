"""Агенты использующие LLM."""

from langchain_core.messages import (
    AIMessage,
    ToolMessage,
    SystemMessage,
    HumanMessage
)
from langchain_core.prompts import PromptTemplate

from main.openai import llm
from main.utils import load_yaml
from main.tools import get_money


def agent_type(data_desc):
    """Агент определяющий тип обращения."""

    system_prompt_path = "prompt_class.yaml"
    system_prompt_text = load_yaml(system_prompt_path)
    system_prompt = system_prompt_text.get("system_prompt")
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Описание обращения: {data_desc}")
    ]
    response = llm.invoke(messages)

    return response


def agent_executor(instruction, data):
    """Агент исполнитель."""

    context = {"data": data,}
    system_prompt_path = "prompt_executor.yaml"
    system_prompt_text = load_yaml(system_prompt_path)
    system_prompt_base = system_prompt_text.get("system_prompt")
    prompt_template = PromptTemplate.from_template(system_prompt_base)
    system_prompt = prompt_template.format(**context)
    tools = [get_money,]
    llm_with_tools = llm.bind_tools(tools)
    tools_map = {tool.name: tool for tool in tools}
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Инструкция: {instruction}")
    ]

    iteration = 0
    max_iterations = 10

    while iteration < max_iterations:
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            return response

        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"Вызываю инструмент: {tool_name} с аргументами: {tool_args}")

            if tool_name in tools_map:
                try:
                    tool_result = tools_map[tool_name].invoke(tool_args)
                    tool_message = ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    )
                    messages.append(tool_message)
                    
                except Exception as e:
                    error_message = ToolMessage(
                        content=f"Ошибка при вызове {tool_name}: {str(e)}",
                        tool_call_id=tool_call["id"]
                    )
                    messages.append(error_message)
            else:
                error_message = ToolMessage(
                    content=f"Инструмент {tool_name} не найден",
                    tool_call_id=tool_call["id"]
                )
                messages.append(error_message)
        
        iteration += 1

    return AIMessage(
        content='{"status": "ERROR", "description": "Превышено максимальное количество итераций"}'
    )
