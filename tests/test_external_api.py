import json
from typing import Any
from typing import Dict
from typing import List
from unittest.mock import Mock
from unittest.mock import patch

import pytest
import requests

from src.external_api import get_amount


@patch("requests.get")
def test_get_amount(mock_get: Mock, transaction_for_conversion: Dict[str, Any], result_of_conversion: str) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = json.loads(result_of_conversion)

    result = get_amount(transaction_for_conversion)
    assert result == 531.307615


@patch("requests.get")
def test_get_amount_bad_status_code(
    mock_get: Mock, transaction_for_conversion: Dict[str, Any], result_of_conversion: str
) -> None:
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.reason = "Not Found"
    mock_response.json.return_value = json.loads(result_of_conversion)
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Client Error")
    mock_get.return_value = mock_response

    with pytest.raises(ConnectionError) as exc_info:
        get_amount(transaction_for_conversion)

    assert str(exc_info.value).startswith("Запрос не был успешным")


def test_get_amount_with_rub(transactions_list: List[Dict[str, Any]]) -> None:
    result = get_amount(transactions_list[2])
    assert result == 43318.34


@patch("requests.get")
def test_get_amount_invalid_result(
    mock_get: Mock, transaction_for_conversion: Dict[str, Any], result_of_conversion_without_result: str
) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = json.loads(result_of_conversion_without_result)

    with pytest.raises(ValueError) as exc_info:
        get_amount(transaction_for_conversion)

    assert str(exc_info.value) == "Ошибка конвертации: Недостаточно данных для конвертации"


@patch("requests.get")
def test_get_amount_with_key_error(mock_get: Mock, transaction_for_conversion_invalid: Dict[str, Any]) -> None:
    with pytest.raises(KeyError) as exc_info:
        get_amount(transaction_for_conversion_invalid)

    assert exc_info.value.args[0] == "Не найдены необходимые данные для конвертации"
