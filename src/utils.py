import json
import logging
import os
from typing import Any, Dict, List, Optional

""" Настройка логгера для модуля utils """

LOG_DIR: str = "logs"
LOG_FILE: str = "utils.log"
os.makedirs(LOG_DIR, exist_ok=True)

log_path: str = os.path.join(LOG_DIR, LOG_FILE)

logger: logging.Logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_path, mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_transaction_data(json_file: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Возвращает пустой список при ошибках.
    """
    if json_file is None:
        logger.debug("Путь к JSON-файлу не указан, возвращаю пустой список.")
        return []

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из {json_file}")
                return data
            else:
                logger.error(f"В файле {json_file} содержится не список.")
    except FileNotFoundError:
        logger.error(f"Файл не найден: {json_file}")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {json_file}")

    return []
