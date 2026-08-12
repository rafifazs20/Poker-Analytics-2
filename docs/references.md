# Research References

## PokerKit

Source: https://github.com/uoftcprg/pokerkit

PokerKit is the mechanics layer for this project, not the strategic brain. It should own:

- No-Limit Texas Hold'em state transitions.
- Betting, calling, folding, blinds, stacks, and board dealing rules.
- Hand evaluation and simulation plumbing.

The DSS layer should own:

- Manual-input schemas.
- Tensor encodings.
- Policy/value models.
- Self-play, regret estimation, and subgame solving.
- Human-readable decision output.

## Libratus Architecture

Primary paper metadata:

- IJCAI: https://www.ijcai.org/Proceedings/2017/772
- Science/PubMed: https://pubmed.ncbi.nlm.nih.gov/29249696/
- CMU overview: https://www.cmu.edu/news/stories/archives/2017/december/ai-inner-workings.html
- Video reference: https://youtu.be/2dX0lwaQRX0

Libratus is the architectural inspiration, but this project is a practical research replica rather than a claim of superhuman parity.

Core modules to imitate:

- Blueprint strategy: compute an approximate Nash-equilibrium base strategy before play.
- Nested subgame solving: refine strategy at reached game states with finer abstractions.
- Self-improvement: identify and fill weaknesses in the blueprint after observing play.

Important translation for this project:

- Sprint 1 should stay focused on exact state capture and reliable tensor mapping.
- Sprint 2 should create self-play trajectories before training sophisticated models.
- Sprint 3 should implement a minimal Deep CFR loop before trying real-time solving.
- Sprint 4 should add bounded look-ahead and value-network assisted subgame solving.
- Sprint 5 should process manual session logs without interacting with poker clients.

## Safety Boundary

The system remains a manual local DSS. It must not inspect, automate, or integrate with poker clients or poker websites.
