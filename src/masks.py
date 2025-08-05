import logging
import os

""" Настройка логгера для модуля masks """

LOG_DIR: str = "logs"
LOG_FILE: str = "masks.log"
os.makedirs(LOG_DIR, exist_ok=True)

log_path: str = os.path.join(LOG_DIR, LOG_FILE)

logger: logging.Logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler(log_path, mode="w")  # перезапись при каждом запуске
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты:
    формат — 'XXXX XX** **** XXXX', где X — открытая цифра, * — маска.
    """
    logger.debug(f"Получен номер карты: {card_number}")
    digits_only: str = card_number.replace(" ", "")
    if len(digits_only) != 16 or not digits_only.isdigit():
        logger.error("Неверный формат номера карты. Требуется 16 цифр.")
        raise ValueError("Ожидается номер карты из 16 цифр")

    first6: str = digits_only[:6]
    last4: str = digits_only[-4:]
    masked: str = f"{first6[:4]} {first6[4:6]}** **** {last4}"
    logger.info(f"Маскированный номер карты: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета:
    формат — '**XXXX', где X — последние 4 цифры, * — маска.
    """
    logger.debug(f"Получен номер счёта: {account_number}")
    digits_only: str = account_number.replace(" ", "")
    if len(digits_only) < 4 or not digits_only.isdigit():
        logger.error("Неверный формат номера счёта. Минимум 4 цифры.")
        raise ValueError("Ожидается номер счёта минимум из 4 цифр")

    masked: str = f"**{digits_only[-4:]}"
    logger.info(f"Маскированный номер счёта: {masked}")
    return masked
