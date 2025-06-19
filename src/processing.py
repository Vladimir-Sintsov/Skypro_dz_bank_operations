from typing import Any, Dict, List

operation_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(operation_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Возвращает новый список операций, отфильтрованный по значению ключа 'state'.
    """
    return [item for item in operation_list if item.get('state') == state]


def sort_by_date(operation_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате (ключ 'date') в порядке от самой новой к самой старой.
    """
    return sorted(operation_list, key=lambda item: item['date'], reverse=True)