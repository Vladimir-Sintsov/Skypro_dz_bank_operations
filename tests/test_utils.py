from unittest.mock import mock_open, patch
from src.utils import get_transaction_data


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_get_transaction_data_valid_file(mock_file):
    transactions = get_transaction_data("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_transaction_data_file_not_found(mock_file):
    transactions = get_transaction_data("data/operation.json")
    assert transactions == []
    mock_file.assert_called_once_with("data/operation.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_get_transaction_data_empty_list(mock_file):
    transactions = get_transaction_data("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_get_transaction_data_invalid_json(mock_file):
    transactions = get_transaction_data("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="100")
def test_get_transaction_data_not_a_list(mock_file):
    transactions = get_transaction_data("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")