def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты:
    формат — 'XXXX XX** **** XXXX', где X — открытая цифра, * — маска.

    """
    digits_only = card_number.replace(" ", "")
    if len(digits_only) != 16 or not digits_only.isdigit():
        raise ValueError("Ожидается номер карты из 16 цифр")

    first6 = digits_only[:6]
    last4 = digits_only[-4:]

    return f"{first6[:4]} {first6[4:6]}** **** {last4}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета:
    формат — '**XXXX', где X — последние 4 цифры, * — маска.

    """
    digits_only = account_number.replace(" ", "")
    if len(digits_only) < 4 or not digits_only.isdigit():
        raise ValueError("Ожидается номер счёта минимум из 4 цифр")

    return f"**{digits_only[-4:]}"
