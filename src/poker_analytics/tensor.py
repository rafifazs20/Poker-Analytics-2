from __future__ import annotations

from poker_analytics.cards import CARD_COUNT, cards_to_mask
from poker_analytics.state import ManualPokerState

POSITIONS = ("SB", "BB", "BTN", "UTG", "HJ", "CO")
STREETS = ("PREFLOP", "FLOP", "TURN", "RIVER")

FEATURE_NAMES = (
    *(f"hole_{index}" for index in range(CARD_COUNT)),
    *(f"board_{index}" for index in range(CARD_COUNT)),
    *(f"position_{position}" for position in POSITIONS),
    *(f"street_{street}" for street in STREETS),
    "pot_bb",
    "hero_stack_bb",
    "effective_stack_bb",
    "opponent_bet_bb",
    "player_count_scaled",
    "pot_odds_required",
)


def state_to_features(state: ManualPokerState) -> list[float]:
    big_blind = state.big_blind
    position_features = [1.0 if state.position == position else 0.0 for position in POSITIONS]
    street_features = [1.0 if state.street == street else 0.0 for street in STREETS]

    return [
        *cards_to_mask(state.hole_cards),
        *cards_to_mask(state.board_cards),
        *position_features,
        *street_features,
        state.pot / big_blind,
        state.hero_stack / big_blind,
        state.effective_stack / big_blind,
        state.opponent_bet / big_blind,
        state.player_count / 6.0,
        state.pot_odds_required,
    ]


def state_to_tensor(state: ManualPokerState):
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for state_to_tensor(). Install with `pip install -e .`.") from exc

    return torch.tensor(state_to_features(state), dtype=torch.float32)

