"""Тесты."""

from dataclasses import dataclass

from main.router import router


@dataclass
class RequestData:
    """Данные запроса для роутера."""

    description: str
    summa: int
    minus: int


test_cases = {
    "test_1": {"description": "я хочу установить банкомат на улице пролетарская в москве", "summa": 1000000, "minus": 400000},
    "test_2": {"description": "я хочу установить банкомат на улице пролетарская в москве", "summa": 1000000, "minus": 6000000},
    "test_3": {"description": "я хочу убрать банкомат на улице пролетарская в москве", "summa": 1000000, "minus": 400000},
    "test_4": {"description": "я хочу убрать банкомат на улице пролетарская в москве", "summa": 1000000, "minus": 6000000},
    "test_5": {"description": "я хочу покататься на вертолете", "summa": 1000000, "minus": 400000}
}


def main_test():
    """Тесты роутера."""

    print("--------------------ТЕСТЫ ЗАПУЩЕНЫ--------------------")
    print()

    for test_name, test_data in test_cases.items():
        request = RequestData(
            description=test_data["description"],
            summa=test_data["summa"],
            minus=test_data["minus"]
        )
        
        print(f"📌 {test_name}")
        print(f"   Описание: {request.description}")
        print(f"   Прибыль: {request.summa}, Расходы: {request.minus}")

        try:
            response = router(request)
            print(f"   Ответ: {response}")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")

        print("-" * 50)


if __name__ == "__main__":
    main_test()
