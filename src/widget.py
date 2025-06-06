from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Функция маскирует номер карты или счёта, сохраняя остальной текст без изменений.

    Примеры:
    'Visa Platinum 7000792289606361' → 'Visa Platinum 7000 79** **** 6361'
    'Счет 73654108430135874305' → 'Счет **4305'
    """
    parts = info.rsplit(' ', 1)
    if len(parts) != 2:
        raise ValueError("Строка должна содержать описание и номер, разделённые пробелом")

    label, number = parts
    if number.isdigit():
        if len(number) == 16:
            masked = get_mask_card_number(number)
        else:
            masked = get_mask_account(number)
        return f"{label} {masked}"
    else:
        raise ValueError("Не найден корректный номер карты или счёта")