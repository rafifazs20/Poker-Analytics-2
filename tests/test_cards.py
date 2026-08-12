import pytest

from poker_analytics.cards import card_index, parse_cards


def test_parse_cards_normalizes_rank_and_suit():
    assert parse_cards("ahKH", expected=2) == ("Ah", "Kh")


def test_parse_cards_rejects_duplicates():
    with pytest.raises(ValueError, match="Duplicate"):
        parse_cards("AhAh")


def test_card_index_is_stable():
    assert card_index("2c") == 0
    assert card_index("As") == 51

