from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
import re


def filter_by_state(transaction: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список операций, отфильтрованный по значению ключа 'state'.
    """
    return [item for item in transaction if item.get("state") == state]


def sort_by_date(transaction: List[Dict[str, Any]], reverse_list: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате (ключ 'date') в порядке от самой новой к самой старой,
    если reverse_list=True (по умолчанию). Если False — сортировка по возрастанию,
    пропускает записи с некорректной или отсутствующей датой.
    """
    valid_items = []

    for item in transaction:
        date_str = item.get("date")
        if isinstance(date_str, str):
            try:
                datetime.fromisoformat(date_str)
                valid_items.append(item)
            except ValueError:
                continue

    return sorted(valid_items, key=lambda items: datetime.fromisoformat(items["date"]), reverse=reverse_list)



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
