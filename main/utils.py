"""Вспомогательные утилиты."""

import os
import yaml


def load_yaml(path_yaml):
    """Утилита для загрузки текста из yaml."""

    base_path = os.path.join(os.path.dirname(__file__), "prompts")
    full_path = os.path.join(base_path, path_yaml)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Файл {full_path} не найден")
    
    with open(full_path, 'r', encoding='utf-8') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Ошибка парсинга YAML в {full_path}: {e}")
