import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7634562893564253", "7634 56** **** 4253"),
    ],
)
def test_get_mask_card(card_number: str, mask_number: str) -> None:
    assert get_mask_card_number(card_number) == mask_number


@pytest.mark.parametrize(
    "number_account, exam_account", [("73654108430135874305", "**4305"), ("73654108430135871856", "**1856")]
)
def test_get_mask_account(number_account: str, exam_account: str) -> None:
    assert get_mask_account(number_account) == exam_account
