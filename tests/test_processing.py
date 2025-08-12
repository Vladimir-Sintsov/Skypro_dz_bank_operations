from typing import Any
from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
from src.processing import get_searched_transactions
from src.processing import get_transactions_count_by_category
from src.processing import sort_by_date


@pytest.mark.parametrize(
    "state, expected_result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_result: List[Dict[str, Any]]) -> None:
    assert filter_by_state(sample_data, state) == expected_result


def test_sort_by_date(unsorted_dates: List[Dict[str, Any]]) -> None:
    expected_sorted_desc = [
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
        {"id": 1, "date": "2018-10-14T08:21:33.419441"},
        {"id": 4, "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(unsorted_dates, reverse=True) == expected_sorted_desc

    expected_sorted_asc = [
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "date": "2018-09-12T21:27:25.241689"},
        {"id": 1, "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
    ]
    # сортировка по возрастанию (от старых к новым)
    assert sort_by_date(unsorted_dates, reverse=False) == expected_sorted_asc


def test_sort_same_dates(same_date: List[Dict[str, Any]]) -> None:
    expected = same_date
    assert sort_by_date(same_date) == expected


def test_sort_with_invalid_dates(unsorted_invalid_dates: List[Dict[str, Any]]) -> None:
    sorted_result = sort_by_date(unsorted_invalid_dates)
    expected_result = [
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sorted_result == expected_result


def test_get_searched_transactions(
    transactions_list: List[Dict[str, Any]], result_transactions_filter: List[Dict[str, Any]]
) -> None:
    result = get_searched_transactions(transactions_list, "Счет")
    assert result == result_transactions_filter


def test_get_searched_transaction_empty_list(transactions_list_empty: List[Dict[str, Any]]) -> None:
    result = get_searched_transactions(transactions_list_empty, "Счет")
    assert result == []


def test_get_searched_transaction_empty_search(transactions_list: List[Dict[str, Any]]) -> None:
    result = get_searched_transactions(transactions_list, "")
    assert result == []


def test_get_searched_transaction_invalid_search(transactions_list: List[Dict[str, Any]]) -> None:
    result = get_searched_transactions(transactions_list, "приветик!")
    assert result == []


def test_get_searched_transaction_without_transactions(sample_data: List[Dict[str, Any]]) -> None:
    result = get_searched_transactions(sample_data, "пупупу")
    assert result == []


def test_get_transactions_count_by_category(transactions_list: List[Dict[str, Any]], category_list: List[str]) -> None:
    result = get_transactions_count_by_category(transactions_list, category_list)
    assert result == {"Перевод организации": 2, "Перевод с карты на карту": 1, "Перевод со счета на счет": 2}


def test_get_transactions_count(transactions_list_empty: List[Dict[str, Any]], category_list: List[str]) -> None:
    result = get_transactions_count_by_category(transactions_list_empty, category_list)
    assert result == {}


def test_get_transactions_without_category(transactions_list: List[Dict[str, Any]]) -> None:
    with pytest.raises(Exception) as exc_info:
        get_transactions_count_by_category(transactions_list, [])

    assert exc_info.value.args[0] == "Список категорий пуст"
