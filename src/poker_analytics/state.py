from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from poker_analytics.cards import parse_cards

Position = Literal["SB", "BB", "BTN", "UTG", "HJ", "CO"]
Street = Literal["PREFLOP", "FLOP", "TURN", "RIVER"]


@dataclass(frozen=True)
class ManualPokerState:
    position: Position
    hole_cards: tuple[str, str]
    board_cards: tuple[str, ...]
    pot: float
    hero_stack: float
    effective_stack: float
    opponent_bet: float
    player_count: int = 6
    small_blind: float = 1.0
    big_blind: float = 2.0

    POSITIONS: ClassVar[tuple[Position, ...]] = ("SB", "BB", "BTN", "UTG", "HJ", "CO")

    @classmethod
    def from_raw(
        cls,
        *,
        position: str,
        hole: str,
        board: str = "",
        pot: float,
        hero_stack: float,
        effective_stack: float,
        opponent_bet: float,
        players: int = 6,
        small_blind: float = 1.0,
        big_blind: float = 2.0,
    ) -> "ManualPokerState":
        normalized_position = position.strip().upper()
        if normalized_position not in cls.POSITIONS:
            raise ValueError(f"Unsupported position: {position!r}")

        hole_cards = parse_cards(hole, expected=2)
        board_cards = parse_cards(board, max_count=5)
        if len(set(hole_cards + board_cards)) != len(hole_cards) + len(board_cards):
            raise ValueError("Hole cards and board cards cannot overlap.")

        return cls(
            position=normalized_position,  # type: ignore[arg-type]
            hole_cards=hole_cards,  # type: ignore[arg-type]
            board_cards=board_cards,
            pot=_non_negative("pot", pot),
            hero_stack=_non_negative("hero_stack", hero_stack),
            effective_stack=_positive("effective_stack", effective_stack),
            opponent_bet=_non_negative("opponent_bet", opponent_bet),
            player_count=_player_count(players),
            small_blind=_positive("small_blind", small_blind),
            big_blind=_positive("big_blind", big_blind),
        )

    @property
    def street(self) -> Street:
        board_count = len(self.board_cards)
        if board_count == 0:
            return "PREFLOP"
        if board_count == 3:
            return "FLOP"
        if board_count == 4:
            return "TURN"
        if board_count == 5:
            return "RIVER"
        raise ValueError("Board must contain 0, 3, 4, or 5 cards.")

    @property
    def pot_odds_required(self) -> float:
        call_amount = min(self.opponent_bet, self.effective_stack)
        denominator = self.pot + call_amount
        if call_amount <= 0 or denominator <= 0:
            return 0.0
        return call_amount / denominator

    def to_summary(self) -> dict[str, object]:
        return {
            "position": self.position,
            "hole_cards": "".join(self.hole_cards),
            "board_cards": "".join(self.board_cards),
            "street": self.street,
            "pot": self.pot,
            "hero_stack": self.hero_stack,
            "effective_stack": self.effective_stack,
            "opponent_bet": self.opponent_bet,
            "player_count": self.player_count,
            "pot_odds_required": round(self.pot_odds_required, 4),
        }


def _non_negative(name: str, value: float) -> float:
    parsed = float(value)
    if parsed < 0:
        raise ValueError(f"{name} must be non-negative.")
    return parsed


def _positive(name: str, value: float) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise ValueError(f"{name} must be positive.")
    return parsed


def _player_count(value: int) -> int:
    parsed = int(value)
    if parsed not in (2, 6):
        raise ValueError("Only heads-up (2) and 6-max (6) are supported in Sprint 1.")
    return parsed

