import json
from typing import Optional, List, Dict, Any


def get_transaction_data(json_file: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Принимает путь до JSON-файла и возвращает список словарей с транзакциями.
    Возвращает пустой список, если файл не найден, пустой, повреждён
    или не содержит список.
    """
    if json_file is None:
        return []

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, FileNotFoundError):
        pass

    return []
