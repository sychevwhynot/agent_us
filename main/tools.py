from langchain_core.tools import tool


@tool
def get_money(summa: int, minus: int) -> int:
    """
    Проверяет экономическую выгоду.
    
    Args:
        summa: Прибыль
        minus: Расходы
    
    Returns:
        dict: Статус установки
    """

    result = summa - minus

    return {"Результат": result}
