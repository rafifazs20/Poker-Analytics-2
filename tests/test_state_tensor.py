import pytest

from poker_analytics.state import ManualPokerState
from poker_analytics.tensor import FEATURE_NAMES, state_to_features


def test_state_derives_flop_and_pot_odds():
    state = ManualPokerState.from_raw(
        position="BTN",
        hole="AhKh",
        board="9hTs9s",
        pot=120,
        hero_stack=980,
        effective_stack=760,
        opponent_bet=80,
        players=6,
    )

    assert state.street == "FLOP"
    assert state.pot_odds_required == pytest.approx(0.4)


def test_state_rejects_impossible_board_count():
    state = ManualPokerState.from_raw(
        position="BB",
        hole="AhKh",
        board="9h",
        pot=20,
        hero_stack=100,
        effective_stack=100,
        opponent_bet=0,
        players=2,
    )

    with pytest.raises(ValueError, match="Board must contain"):
        _ = state.street


def test_tensor_feature_shape_matches_names():
    state = ManualPokerState.from_raw(
        position="CO",
        hole="AsAd",
        board="",
        pot=3,
        hero_stack=200,
        effective_stack=200,
        opponent_bet=2,
        players=6,
    )

    features = state_to_features(state)
    assert len(features) == len(FEATURE_NAMES)
    assert sum(features[:52]) == 2.0
    assert sum(features[52:104]) == 0.0

