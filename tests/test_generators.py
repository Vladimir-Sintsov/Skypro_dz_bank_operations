import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions



def test_filter_by_currency(transactions_list):
    gen = filter_by_currency(transactions_list, "USD")
    assert next(gen) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_invalid_currency(transactions_list_invalid):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(transactions_list_invalid, "USD"))
    assert exc_info.value.args[0] == "Операции в заданной валюте не найдены"


def test_filter_by_currency_without_key(transactions_list_without_key):
    with pytest.raises(KeyError) as exc_info:
        list(filter_by_currency(transactions_list_without_key, "RUB"))
    assert exc_info.value.args[0] == "Информация о валюте отсутствует"


def test_filter_by_invalid_currency_empty(transactions_list_empty):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(transactions_list_empty, "RUB"))
    assert str(exc_info.value) == "Список транзакций пуст"


def test_transaction_descriptions(transactions_list):
    gen = transaction_descriptions(transactions_list)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"


def test_transaction_descriptions_missing_key():
    transactions = [
        {"id": 1},
        {"id": 2, "description": "Операция по карте"},
    ]
    result = list(transaction_descriptions(transactions))
    assert result == ["", "Операция по карте"]


def test_transaction_descriptions_empty(transactions_list_empty):
    assert list(transaction_descriptions(transactions_list_empty)) == []


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (
            1,
            11,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
            ],
        )
    ],
)
def test_card_number_generator(start, stop, expected_numbers):
    number = list(card_number_generator(start, stop))
    assert number == expected_numbers


def test_card_number_generator_finally():
    number = card_number_generator(9999999999999998, 9999999999999999)
    assert next(number) == "9999 9999 9999 9998"
    assert next(number) == "9999 9999 9999 9999"


def test_card_number_generator_finally_else():
    number = card_number_generator(9999999999999999, 10000000000000000000)
    assert next(number) == "9999 9999 9999 9999"


@pytest.mark.parametrize(
    "start, end, expected_numbers",
    [
        (100, 101, ["0000 0000 0000 0100", "0000 0000 0000 0101"]),
        (102, 103, ["0000 0000 0000 0102", "0000 0000 0000 0103"]),
    ],
)
def test_card_gen_use_parametrize(start, end, expected_numbers):
    result = list(card_number_generator(start, end))
    assert result == expected_numbers


def test_card_gen_invalid_parameters():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(2, 1))
    assert str(exc_info.value) == "Ошибка: Start не должен превышать Stop"


def test_filter_by_currency_with_xlsx_csv(csv_data_result):
    gen = filter_by_currency(csv_data_result, "COP")
    assert next(gen) == {
        "amount": "29740",
        "currency_code": "COP",
        "currency_name": "Peso",
        "date": "2020-12-06T23:00:58Z",
        "description": "Перевод с карты на карту",
        "from": "Discover 3172601889670065",
        "id": "3598919",
        "state": "EXECUTED",
        "to": "Discover 0720428384694643",
    }

@pytest.fixture
def csv_data_result():
    return [
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

