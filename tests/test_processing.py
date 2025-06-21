from typing import Any
from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
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
    assert sort_by_date(unsorted_dates) == expected_sorted_desc

    expected_sorted_asc = [
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "date": "2018-09-12T21:27:25.241689"},
        {"id": 1, "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(unsorted_dates, reverse_list=False) == expected_sorted_asc


def test_sort_same_dates(same_date: List[Dict[str, Any]]) -> None:
    expected = same_date
    assert sort_by_date(same_date) == expected


def test_sort_with_invalid_dates(unsorted_invalid_dates: List[Dict[str, Any]]) -> None:
    sorted_result = sort_by_date(unsorted_invalid_dates)
    expected_result = [
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sorted_result == expected_result
