import csv
import logging
import os
from typing import Dict
from typing import List
from typing import Optional

import pandas as pd

# Настройка логирования по вашему примеру
LOG_DIR: str = "logs"
LOG_FILE: str = "csv_xlsx_utils.log"
os.makedirs(LOG_DIR, exist_ok=True)

log_path: str = os.path.join(LOG_DIR, LOG_FILE)

logger: logging.Logger = logging.getLogger("csv_xlsx_utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_path, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_csv(csv_path: Optional[str]) -> List[Dict]:
    """
    Считывает финансовые операции из CSV файла.
    Возвращает список словарей с транзакциями.
    """
    if not csv_path:
        logger.warning("Путь к CSV файлу не указан.")
        return []

    try:
        with open(csv_path, mode="r", encoding="utf-8") as f:
            result_dict = csv.DictReader(f, delimiter=";")
            logger.info(f"Успешно считан CSV файл: {csv_path}")
            return list(result_dict)
    except (FileNotFoundError, csv.Error) as e:
        logger.error(f"Ошибка при чтении CSV файла '{csv_path}': {e}")
        return []


def get_excel(excel_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel файла.
    Возвращает список словарей с транзакциями.
    :rtype: List[Dict]
    """
    try:
        df = pd.read_excel(excel_path)
        if isinstance(df, pd.DataFrame) and not df.empty:
            logger.info(f"Успешно считан Excel файл: {excel_path}")
            return df.to_dict(orient="records")
        else:
            logger.warning(f"Excel файл пуст или не содержит данных: {excel_path}")
            return []
    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {excel_path} - {e}")
        return []
    except ValueError as e:
        logger.error(f"Ошибка при чтении Excel файла '{excel_path}': {e}")
        return []
