from __future__ import annotations

import argparse
import json

from poker_analytics.state import ManualPokerState
from poker_analytics.tensor import FEATURE_NAMES, state_to_features


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="poker-analytics")
    subparsers = parser.add_subparsers(dest="command", required=True)

    quick = subparsers.add_parser("quick", help="Validate a manually entered poker state.")
    quick.add_argument("--position", required=True, help="Hero position: SB, BB, BTN, UTG, HJ, or CO.")
    quick.add_argument("--hole", required=True, help="Two-card hand, for example AhKh.")
    quick.add_argument("--board", default="", help="Board cards, for example 9hTs9s.")
    quick.add_argument("--pot", required=True, type=float)
    quick.add_argument("--hero-stack", required=True, type=float)
    quick.add_argument("--effective-stack", required=True, type=float)
    quick.add_argument("--opponent-bet", required=True, type=float)
    quick.add_argument("--players", default=6, type=int, choices=(2, 6))
    quick.add_argument("--small-blind", default=1.0, type=float)
    quick.add_argument("--big-blind", default=2.0, type=float)
    quick.add_argument("--features", action="store_true", help="Include numeric feature vector metadata.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "quick":
        state = ManualPokerState.from_raw(
            position=args.position,
            hole=args.hole,
            board=args.board,
            pot=args.pot,
            hero_stack=args.hero_stack,
            effective_stack=args.effective_stack,
            opponent_bet=args.opponent_bet,
            players=args.players,
            small_blind=args.small_blind,
            big_blind=args.big_blind,
        )
        payload = state.to_summary()
        if args.features:
            features = state_to_features(state)
            payload["feature_count"] = len(features)
            payload["expected_feature_count"] = len(FEATURE_NAMES)
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    parser.error(f"Unsupported command: {args.command}")
    return 2

