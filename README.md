### Как запустить проект

1. Установить Python 3.12 - [Скачать с официального сайта](https://www.python.org/downloads/release/python-31210/)
2. Клонировать репозиторий - `git clone git@github.com:sychevwhynot/agent_us.git`
3. Создать виртуальное окружение в корневой директории - `python -m venv venv`
4. Запустить вирутальное окружение - `source venv/Scripts/activate`
5. Обновить pip - `python -m pip install --upgrade pip`
6. Установить зависимости - `pip install -r requirements.txt`
7. Запустить тесты - `python test.py`

### Структура проекта

```bash
agent_test/
├── main/
│   ├── __init__.py
│   ├── agents.py              # Агенты (классификатор + исполнитель)
│   ├── router.py              # Роутер, управляющий агентами
│   ├── openai.py              # Настройка LLM (Deepseek)
│   ├── utils.py               # Утилиты (загрузка YAML)
│   ├── tools.py               # Инструменты для агентов
│   └── prompts/               # YAML-файлы с промптами
│       ├── prompt_class.yaml          # Промпт для классификации
│       ├── prompt_executor.yaml       # Промпт для исполнителя
│       ├── instruction_install.yaml   # Инструкция по установке
│       └── instruction_uninstall.yaml # Инструкция по демонтажу
├── test.py                    # Тестовый скрипт
├── requirements.txt           # Зависимости
└── README.md
```