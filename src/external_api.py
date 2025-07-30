import os
from typing import Any
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях.
    Если валюта не рубли — конвертирует с помощью внешнего API.
    """
    try:
        operation = transaction["operationAmount"]
        currency = operation["currency"]["code"]
        amount = float(operation["amount"])

        if currency == "RUB":
            return amount

        if not API_KEY:
            raise EnvironmentError("API_KEY не найден в переменных окружения")

        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"to": "RUB", "from": currency, "amount": amount}
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        result = data.get("result")

        if result is None:
            raise ValueError("Недостаточно данных для конвертации")

        return float(result)

    except KeyError:
        raise KeyError("Не найдены необходимые данные для конвертации")
    except requests.RequestException as e:
        raise ConnectionError(f"Запрос не был успешным. Возможная причина: {e}")
    except ValueError as e:
        raise ValueError(f"Ошибка конвертации: {e}")
