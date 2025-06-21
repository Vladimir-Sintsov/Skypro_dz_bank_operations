from typing import Any
from typing import Dict
from typing import List

import pytest


@pytest.fixture
def card_data() -> list:
    return [("7000792289606361", "7000 79** **** 6361"), ("7634562893564253", "7634 56** **** 4253")]


@pytest.fixture
def account_data() -> list:
    return [("73654108430135874305", "**4305"), ("73654108430135871856", "**1856")]


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def same_date() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2022-01-01T12:00:00"},
        {"id": 2, "date": "2022-01-01T12:00:00"},
        {"id": 3, "date": "2022-01-01T12:00:00"},
    ]


@pytest.fixture
def unsorted_dates() -> list[dict[str, Any]]:
    return [
        {"id": 1, "date": "2018-10-14T08:21:33.419441"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
        {"id": 4, "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def unsorted_invalid_dates() -> list[dict[str, Any]]:
    return [
        {"id": 1, "date": "invalid-date"},
        {"id": 2, "date": None},
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
        {"id": 4},  # нет ключа date
    ]
