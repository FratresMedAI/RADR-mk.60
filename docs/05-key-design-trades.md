# 05 — Key Design Trades

**Document ID:** RADR / DOC-05  
**Version:** 0.7.0  
**Status:** Conceptual

---

## Locked Trades (Current Baseline)

| Trade | Selection | Rationale |
|-------|-----------|-----------|
| Mission focus | **Squad / SOF** terminal C-UAS | Not divisional SAM |
| Primary virtue | **Speed-to-target** | Less evasion time |
| Guidance | **Low-maneuver** nose canards | KISS; pairs with rough aim |
| Off-boresight | **Rejected** | Cost, complexity, drag |
| Warhead | **Ti/steel cube forward cone** | Drone structures are fragile |
| Fuze | **Proximity + timed backup** | Reliability without seeker fuze |
| Motor | **Progressive burn** | Manage recoil; ramp for range |
| Caliber | **60 mm** | Cube pack + motor + seeker |
| Rocket length | **18 in max** | Performance vs. portability |
| Launcher | **36 in** reusable | Breech + backblast + balance |
| Breech | **Gustav flip + deadbolt** | Familiar; positive lock |
| Round | **Ravioli-can tube** | Field ruggedness |
| Controls | **Dual-trigger + tone** | Safe arm sequence |
| Sights | **Holographic square** | Fast aim; thermal optional |
| CoG | **Rear-biased** | Shoulder comfort |

---

## Speed vs. Agility

| Approach | RADR choice |
|----------|------------|
| High-maneuver / OBA | **Rejected** — adds mass, cost, software risk |
| Speed-first + small canards | **Selected** — matches drone threat timeline |

The rocket is optimized to **arrive quickly**, not to fly aggressive intercept spirals.

---

## Motor: Progressive Burn

| Phase | Behavior |
|-------|----------|
| First **1–2 s** | **Lower thrust** — manageable recoil/backblast |
| Ramp | Increasing thrust for **terminal velocity** at range |

Neutral or boost-first grains were traded away for **gunner safety** and **shoulderability**.

---

## Fuze: Proximity + Timed Backup

| Layer | Role |
|-------|------|
| **Proximity (primary)** | Actuate at **~20 ft** for forward cone |
| **Timed (backup)** | Failsafe if proximity misses — still produces lethal cloud |

Seeker-gated fuze was rejected as unnecessary complexity for this envelope.

---

## Warhead: Cone vs. Omnidirectional

**Forward cone** (~10–12 ft @ ~20 ft) concentrates fragments on the threat axis — better than a spherical cloud for a **rough-aimed** weapon.

---

## Removed from Program

| Element | Status |
|---------|--------|
| Laser beam-riding | Removed |
| Launcher-tracked guidance | Removed |
| Kinetic penetrator rod | Removed |
| FMCW radar seeker | Not baseline |
| High off-boresight autopilot | Rejected |

---

[← CONOPS](04-conops-use-cases.md) | [Next: System Description →](06-system-description.md)
