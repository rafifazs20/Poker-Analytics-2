from __future__ import annotations

from poker_analytics.tensor import FEATURE_NAMES

ACTION_NAMES = ("fold", "call", "raise_half_pot", "raise_pot", "all_in")


def build_policy_network(hidden_size: int = 256):
    try:
        import torch.nn as nn
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for model scaffolding. Install with `pip install -e .`.") from exc

    return nn.Sequential(
        nn.Linear(len(FEATURE_NAMES), hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, hidden_size),
        nn.ReLU(),
        nn.Linear(hidden_size, len(ACTION_NAMES)),
    )

