# RADR — Lightweight Recoilless Anti-Drone System

**Terminal Counter-UAS — 60 mm Class**

A lightweight, reusable **60 mm** shoulder-fired rocket system for **squad and SOF** use. It fires an **18-inch** rocket with a **Ti/steel cube flak** warhead, **onboard IR fire-and-forget** seeker, and **progressive-burn** motor optimized for **speed-to-target** rather than high off-boresight maneuvering. The design emphasizes **simplicity, reliability, and one-person reload**.

**Status:** Phase 0 — Conceptual (refined baseline v0.7)  
**Version:** 0.7.0  

---

## Core Vision

RADR is a **fast terminal flak** weapon: the gunner **rough-aims**, the seeker **locks** (audible tone), and the rocket **closes quickly** with **small canard corrections** only. At **~20 ft** from the target, a **proximity-primary fuze** (with **timed backup**) disperses **300 rough-edged Ti/steel cubes** in a **forward cone**. The small burster **disperses** — the **cubes kill**.

**Philosophy:** Speed is the primary defense · KISS + rugged · Not high off-boresight · Honest capability ceiling.

---

## Locked Specifications

| Item | Spec | Status |
|------|------|--------|
| Caliber | 60 mm | Locked |
| Rocket length | 18 in (457 mm) max | Locked |
| Launcher length | 36 in (914 mm) | Locked |
| Rocket mass | ≤ 3.5 kg | Locked |
| Launcher empty mass | ≤ 5.5 kg | Locked |
| Warhead | 300 × 7 mm dense alloy rough-edged cubes (Ti/steel) | Locked |
| Pattern | Forward cone, ~10–12 ft wide @ ~20 ft | Locked |
| Fuze | **Proximity primary + timed backup** | Locked |
| Seeker | 100 mm IR fire-and-forget | Locked |
| Guidance | Low-maneuver; small movable canards near nose | Locked |
| Fins | 4 swept spring-loaded at base; deploy on exit | Locked |
| Motor | Progressive burn (lower thrust 1–2 s, then ramp) | Locked |
| Range | 1000 m effective | Goal |
| Backblast | ≤ 10 yards (30 ft) | Locked |
| Protective tube | “Ravioli can” + pull-off cap (soldier removes on load) | Locked |
| Breech | Gustav-style flip + spring bolt + deadbolt lock | Locked |
| Controls | Front = seeker + lock tone; rear = fire (front held) | Locked |
| CoG | Slightly rear-biased (shouldering comfort) | Locked |
| Sights | Advanced holographic (square reticle); thermal overlay TBD | Locked / evolving |

---

## Operational Flow

1. **Open breech** — pull spring bolt, swing open.  
2. **Pop top** off protective tube (“ravioli can”).  
3. **Load tube** into launcher.  
4. **Close breech** — auto-locks (deadbolt-style).  
5. **Hold front trigger** — seeker on; **audible tone** when locked.  
6. **Pull rear trigger** (front held) — launch.  
7. Rocket flies **fast**; fins deploy; **small nose canard** trims only.  
8. **~20 ft** — proximity fuze (timed backup) → **forward cone** of cubes.  
9. **Open breech** — empty tube drops out → repeat.

**Carry:** Launcher + one round ≤ **9.0 kg** — one person can reload.

---

## Rocket Mass (Notional — under 3.5 kg cap)

| Component | Mass (kg) |
|-----------|-----------|
| Warhead (cubes + burster + casing) | 0.95–1.15 |
| IR seeker + avionics (100 mm) | 0.45–0.55 |
| Motor + propellant | 1.10–1.30 |
| Structure, fins, canards, nozzle | 0.35–0.45 |
| **Total** | ≤ **3.5 kg** |

---

## Motor (Notional — 1000 m goal)

| Parameter | Value |
|-----------|--------|
| Grain | Progressive: **lower thrust 1–2 s**, then ramp |
| Propellant | ~1.15–1.25 kg; ~260 mm grain |
| Burn time | ~3.0–3.4 s |
| Terminal velocity @ 1000 m | ~330–370 m/s (estimate) |

*Notional until live fire.*

---

## Comparison Snapshot

| | RADR | Carl Gustaf M4 | FIM-92 Stinger |
|--|-----------|----------------|----------------|
| Launcher | ≤ 5.5 kg, 36 in | ~6.6 kg | ~15 kg system |
| Round | ≤ 3.5 kg, 18 in | ~3.2 kg | ~10.1 kg |
| Guidance | IR F&F, low-maneuver | Unguided | IR, high agility |
| Range (design) | 1000 m | ammo-dependent | 4000+ m |
| Backblast | 10 yd (30 ft) | ~60 m class | moderate |

Data: [`data/baseline_systems.json`](data/baseline_systems.json)

---

## Rejected / Out of Scope

Laser beam-riding · Launcher-tracked guidance · Kinetic penetrator rod · High off-boresight agility · Pre-fire BIT complexity · Every-rifleman issue

---

## Document Map

| # | Document |
|---|----------|
| 01 | [Concept Overview](docs/01-concept-overview.md) |
| 02 | [Operational Requirements](docs/02-operational-requirements.md) |
| 03 | [Design Constraints](docs/03-design-constraints.md) |
| 04 | [CONOPS / Use Cases](docs/04-conops-use-cases.md) |
| 05 | [Key Design Trades](docs/05-key-design-trades.md) |
| 06 | [System Description](docs/06-system-description.md) |
| 07 | [Limitations and Risks](docs/07-limitations-and-risks.md) |
| 08 | [Layered Defense Integration](docs/08-layered-defense-integration.md) |

Annexes A–E: [`annexes/`](annexes/)

---

## Open Questions

- Holographic sight vendor / square reticle harmonization with seeker FOV  
- Basic thermal overlay: cost vs. squad benefit  
- Live-fire Pk at 1000 m (hover vs. crossing)  
- Progressive grain qualification vs. backblast at 10 yd zone  

---

## Disclaimer

Conceptual engineering study only. Mass, motor, range, and lethality figures are **notional** until tested. Not authorization for procurement or use.
