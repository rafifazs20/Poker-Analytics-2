from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PokerKitConfig:
    player_count: int = 6
    small_blind: int = 1
    big_blind: int = 2
    starting_stack: int = 200
    ante: int = 0


def create_empty_holdem_state(config: PokerKitConfig):
    try:
        from pokerkit import Automation, NoLimitTexasHoldem
    except ImportError as exc:
        raise RuntimeError("PokerKit is required for mechanics integration. Install with `pip install -e .`.") from exc

    automations = (
        Automation.ANTE_POSTING,
        Automation.BET_COLLECTION,
        Automation.BLIND_OR_STRADDLE_POSTING,
        Automation.CARD_BURNING,
        Automation.HOLE_DEALING,
        Automation.BOARD_DEALING,
        Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
        Automation.HAND_KILLING,
        Automation.CHIPS_PUSHING,
        Automation.CHIPS_PULLING,
    )
    return NoLimitTexasHoldem.create_state(
        automations,
        True,
        config.ante,
        (config.small_blind, config.big_blind),
        config.big_blind,
        tuple(config.starting_stack for _ in range(config.player_count)),
        config.player_count,
    )

