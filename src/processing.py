import re
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список операций, отфильтрованный по значению ключа 'state'.
    """
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате (ключ 'date') в порядке от самой новой к самой старой,
    если reverse=True. Если False — сортировка по возрастанию.
    Пропускает записи с некорректной или отсутствующей датой.
    """
    valid_items = []

    for item in transactions:
        date_str = item.get("date")
        if isinstance(date_str, str):
            try:
                # Проверка валидности даты
                datetime.fromisoformat(date_str)
                valid_items.append(item)
            except ValueError:
                continue  # пропускаем некорректные даты

    # Сортируем только валидные записи
    return sorted(valid_items, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)


def get_searched_transactions(transactions: list, search_str: str) -> List[dict]:
    """
    Возвращает список транзакций, у которых в описании есть строка search_str (игнорируя регистр).
    """
    if not search_str:
        return []

    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    result = []

    for transaction in transactions:
        if "description" in transaction:
            if re.search(pattern, transaction["description"]):
                result.append(transaction)
        # Если ключа нет, пропускаем транзакцию

    return result


def get_transactions_count_by_category(transactions: list, category_list: list) -> dict:
    """
    Возвращает словарь с количеством транзакций по каждой категории.
    """
    if not category_list:
        raise Exception("Список категорий пуст")

    result = {}

    for category in category_list:
        pattern = re.compile(re.escape(category), flags=re.IGNORECASE)
        counter = 0

        for transaction in transactions:
            if "description" in transaction:
                if re.search(pattern, transaction["description"]):
                    counter += 1

        if counter > 0:
            result[category] = counter

    return result
