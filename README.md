# Poker Analytics 2

Manual-input Poker Decision Support System research scaffold for No-Limit Texas Hold'em.

This project is intentionally designed as a local, manual DSS. It does not read poker client screens, scrape memory, automate browser/game clients, or call poker-site APIs.

## Sprint 1 Scope

- Python package foundation under `src/poker_analytics`.
- Fast CLI scaffold for manually entering game state.
- Card and state validation.
- Tensor feature mapping for future PyTorch policy/value networks.
- Optional PokerKit adapter for No-Limit Texas Hold'em mechanics.

## Research References

- PokerKit: https://github.com/uoftcprg/pokerkit
- Libratus talk/video reference: https://youtu.be/2dX0lwaQRX0
- Reference notes: [docs/references.md](docs/references.md)

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the manual-input CLI:

```powershell
poker-analytics quick --position BTN --hole AhKh --board 9hTs9s --pot 120 --hero-stack 980 --effective-stack 760 --opponent-bet 80 --players 6
```

Without installing the package, from the repo root:

```powershell
$env:PYTHONPATH="src"; python -m poker_analytics quick --position BTN --hole AhKh --board 9hTs9s --pot 120 --hero-stack 980 --effective-stack 760 --opponent-bet 80 --players 6
```

## GitHub Remote

This repository tracks:

```text
https://github.com/rafifazs20/Poker-Analytics-2.git
```

If this checkout ever needs to be reconnected:

```powershell
git remote add origin <repo-url>
git push -u origin main
```
