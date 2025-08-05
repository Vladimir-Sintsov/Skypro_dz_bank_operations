from unittest.mock import mock_open
from unittest.mock import patch
from typing import List, Dict, Any

import pandas as pd

from src.csv_xlsx_utils import get_csv
from src.csv_xlsx_utils import get_excel


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=(
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
        "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;"
        "Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"
    ),
)
def test_csv_reader(mock_file: Any) -> None:
    """
    Тестирует функцию get_csv для корректного чтения CSV файла.
    Мокаем содержимое файла и проверяем, что функция возвращает правильный список словарей.
    """
    # Вызов функции
    transactions: List[Dict[str, str]] = get_csv("data/transactions.csv")
    # Проверка, что результат совпадает с ожидаемым
    expected: List[Dict[str, str]] = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    assert transactions == expected
    mock_file.assert_called_once_with("data/transactions.csv", mode="r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_csv_invalid(mock_file: Any) -> None:
    """
    Тестирует функцию get_csv при пустом файле.
    Ожидается, что функция вернет пустой список.
    """
    transactions: List[Dict[str, str]] = get_csv("data/transactions.csv")
    assert transactions == []
    mock_file.assert_called_once_with("data/transactions.csv", mode="r", encoding="utf-8")


def test_read_csv_invalid_path() -> None:
    """
    Тестирует функцию get_csv при несуществующем пути.
    Ожидается, что функция вернет пустой список.
    """
    transactions: List[Dict[str, str]] = get_csv("some/invalid/path")
    assert transactions == []


def test_read_csv_not_path() -> None:
    """
    Тестирует функцию get_csv при пустом пути.
    Ожидается, что функция вернет пустой список.
    """
    transactions: List[Dict[str, str]] = get_csv("")
    assert transactions == []


@patch("pandas.read_excel")
def test_get_excel(mock_read_excel: Any, excel_data: Dict[str, List[Any]], excel_data_result: List[Dict[str, Any]]) -> None:
    """
    Тест функции get_excel: проверяет чтение Excel и возврат DataFrame.
    Мокирует pandas.read_excel для возврата фикстурных данных.
    """
    mock_read_excel.return_value = pd.DataFrame(excel_data)
    result: List[Dict[str, Any]] = get_excel("..\\data\\transactions.xlsx")
    assert result == excel_data_result


@patch("pandas.read_excel")
def test_get_excel_empty(mock_read_excel: Any) -> None:
    """
    Тестирует функцию get_excel при возврате пустого DataFrame.

    Ожидается, что функция вернет пустой список.
    """
    mock_read_excel.return_value = pd.DataFrame()

    result: List[Dict[str, Any]] = get_excel("files/some_file.xlsx")

    assert result == []


def test_get_excel_no_path() -> None:
    """
    Тестирует функцию get_excel при пустом пути.

    Ожидается, что функция вернет пустой список.
    """
    result: List[Dict[str, Any]] = get_excel("")

    assert result == []


def test_get_excel_invalid_path() -> None:
     """
     Тестирует функцию get_excel при неправильном или несуществующем файле.

     Ожидается, что функция вернет пустой список.
     """
     result: List[Dict[str, Any]] = get_excel("files/some_file.xlsx")

     assert result == []