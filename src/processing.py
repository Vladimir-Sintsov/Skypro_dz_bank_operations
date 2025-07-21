from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

transaction_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


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
