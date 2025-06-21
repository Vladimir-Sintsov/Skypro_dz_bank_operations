import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "exam_account_card, hide_account",
    [
        ("Visa Platinun 7008792289606361", "Visa Platinun 7008 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(exam_account_card: str, hide_account: str) -> None:
    assert mask_account_card(exam_account_card) == hide_account


@pytest.mark.parametrize(
    "exam_date, new_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ],
)
def test_get_date(exam_date: str, new_date: str) -> None:
    assert get_date(exam_date) == new_date
