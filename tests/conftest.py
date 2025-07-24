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


@pytest.fixture
def transactions_list() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_list_invalid() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "GBP", "code": "GBP"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "GBP"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_list_without_key() -> list[dict[str, Any]]:
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "GBP"},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "amount": "56883.54",
            "currency": {"name": "RUB", "code": "RUB"},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_list_empty() -> List[Dict[str, Any]]:
    return []


@pytest.fixture
def transaction_for_conversion() -> Dict[str, Any]:
    return {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {"amount": "5", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    }


@pytest.fixture
def result_of_conversion() -> str:
    return """{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "USD",
    "to": "RUB"
  },
  "result": 531.307615,
  "success": true
}"""


@pytest.fixture
def result_of_conversion_without_result() -> str:
    return """{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "USD",
    "to": "RUB"
  },
  "success": true
}"""


@pytest.fixture
def transaction_for_conversion_invalid() -> Dict[str, Any]:
    return {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {
            "amount": "5",
        },
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    }


@pytest.fixture
def transaction_rub() -> Dict[str, Any]:
    return {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2023-07-24T10:00:00",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Оплата услуг",
        "from": "Счет 12345678901234567890",
        "to": "Счет 09876543210987654321",
    }
