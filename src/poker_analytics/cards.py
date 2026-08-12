from __future__ import annotations

RANKS = "23456789TJQKA"
SUITS = "cdhs"
CARD_COUNT = 52


def normalize_card(card: str) -> str:
    value = card.strip()
    if len(value) != 2:
        raise ValueError(f"Card must have exactly 2 characters: {card!r}")

    rank = value[0].upper()
    suit = value[1].lower()
    if rank not in RANKS:
        raise ValueError(f"Invalid card rank: {value[0]!r}")
    if suit not in SUITS:
        raise ValueError(f"Invalid card suit: {value[1]!r}")
    return f"{rank}{suit}"


def parse_cards(raw: str, *, expected: int | None = None, max_count: int | None = None) -> tuple[str, ...]:
    value = raw.strip()
    if not value:
        cards: tuple[str, ...] = ()
    else:
        if len(value) % 2 != 0:
            raise ValueError("Card string must contain pairs like AhKh or 9hTs9s.")
        cards = tuple(normalize_card(value[index : index + 2]) for index in range(0, len(value), 2))

    if expected is not None and len(cards) != expected:
        raise ValueError(f"Expected {expected} cards, got {len(cards)}.")
    if max_count is not None and len(cards) > max_count:
        raise ValueError(f"Expected at most {max_count} cards, got {len(cards)}.")
    if len(set(cards)) != len(cards):
        raise ValueError("Duplicate cards are not allowed.")
    return cards


def card_index(card: str) -> int:
    normalized = normalize_card(card)
    rank_index = RANKS.index(normalized[0])
    suit_index = SUITS.index(normalized[1])
    return suit_index * len(RANKS) + rank_index


def cards_to_mask(cards: tuple[str, ...]) -> list[float]:
    mask = [0.0] * CARD_COUNT
    for card in cards:
        mask[card_index(card)] = 1.0
    return mask

