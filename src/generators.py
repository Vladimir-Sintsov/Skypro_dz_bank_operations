from typing import Any
from typing import Dict
from typing import Generator
from typing import Iterable
from typing import List


def filter_by_currency(info_list: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """
    Функция, находящая операции в заданной валюте
    """
    if not info_list:
        raise ValueError("Список транзакций пуст")

    def is_match(txn: Dict[str, Any]) -> bool:
        if "operationAmount" in txn:
            currency_code = txn.get("operationAmount", {}).get("currency", {}).get("code")
            return currency_code == currency if currency_code is not None else False
        elif "currency_code" in txn:
            currency_code = txn.get("currency_code")
            return currency_code == currency if currency_code is not None else False
        else:
            raise KeyError("Информация о валюте отсутствует")

    filtered = (txn for txn in info_list if is_match(txn))
    first = next(filtered, None)

    if not first:
        raise ValueError("Операции в заданной валюте не найдены")

    yield first
    yield from filtered


def transaction_descriptions(info_list: Iterable[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Генератор описаний операций из списка
    """
    for x in info_list:
        yield x.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт в 16-значном формате с пробелами
    """
    if start > stop:
        raise ValueError("Ошибка: Start не должен превышать Stop")

    for number in range(start, stop + 1):
        number_str = str(number).zfill(16)
        yield f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
