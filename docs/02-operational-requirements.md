# 02 — Operational Requirements

**Document ID:** TKI-30-66 / DOC-02  
**Version:** 0.4.0  
**Status:** Conceptual

Full KPP tables: [Annex B — KPP Targets](../annexes/B-kpp-targets.md)

---

## Primary Mission

Provide dismounted squad and SOF elements the capability to **defeat or mission-kill small-to-medium UAS** (approximately 2–25 kg class) at close-to-mid range by delivering a **guided Ti BB flak cloud** in the target's flight path, under direct team control, without external laser designation or higher-echelon interceptors.

---

## Key Performance Parameters (KPPs)

### Must-Have (Threshold)

| Parameter | Threshold | Rationale |
|-----------|-----------|-----------|
| Launcher mass (empty) | ≤ 7.5 kg | Single gunner carry |
| Ready rocket mass | ≤ 2.8 kg | Lightweight; ammo bearer carries 2–4 |
| Ready rocket OAL | ≤ 457 mm (18 in) | User upper bound; pack volume |
| Nominal caliber | 40–66 mm envelope (50 mm baseline) | Sub-Gustaf form factor |
| Warhead type | Ti BB flak dispersal | Core concept |
| Guidance | Onboard IR, fire-and-forget | No beam-riding |
| Effective range vs. 2–25 kg UAS | ≥ 150 m min / ≥ 600 m design | Terminal layer |
| Rear danger zone (backblast) | ≤ 40 m | Squad employment |
| Cost per rocket (production goal) | ≤ $500 | Below missile class |
| Seeker lock before fire | Required | Gunner confirms lock indicator |
| Dispersal function | ≥ 98% of rockets (factory QA) | Dud flak unacceptable |

### Should-Have (Objective)

| Parameter | Objective | Rationale |
|-----------|-----------|-----------|
| Launcher mass (empty) | ≤ 7.0 kg | Lighter carry |
| Ready rocket mass | ≤ 2.3 kg | More rounds per bearer |
| Effective range | ≥ 800 m (cooperative hover, clear IR) | Aspirational |
| Single-shot Pk vs. hover (Group 1) | ≥ 0.50 | Cloud coverage dependent |
| Single-shot Pk vs. crossing 90° | ≥ 0.25 | Honest hard geometry |
| Time to first shot | ≤ 15 s from ready carry | Ambush response |
| Reload time | ≤ 10 s (trained gunner) | Volume of fire |
| Sustained rate of fire | 4–6 rockets / 2 min (2-man team) | Swarm response |
| Rear danger zone | ≤ 30 m | Gustaf improvement |
| Cost per rocket | ≤ $300 | Volume target |

---

## Secondary Requirements

| Requirement | Description |
|-------------|-------------|
| Night employment | IR seeker exploits UAS thermal signature |
| Training burden | ≤ Carl Gustaf basic + MANPADS-style lock discipline |
| No external designator | Gunner-only lock and fire |
| Environmental | -25 to +45 °C operating |
| Storage | ≥ 10 years sealed rocket; small-arms logistics chain |
| Collateral awareness | BB hazard footprint documented for ROE |

---

## Target Set Definition

| Target Class | Mass | Examples | Priority |
|--------------|------|----------|----------|
| Group 1 (small) | < 9 kg | Quadcopters, FPV | Primary |
| Group 2 (medium) | 9–25 kg | ISR, larger FPV | Primary |
| Group 3 (large) | > 25 kg | Tactical UAS | Secondary |
| Fast fixed-wing | Any | Racing-wing | Limited Pk |

---

## Measures of Effectiveness (MOE)

| MOE | Metric | Notional Target |
|-----|--------|-----------------|
| Threat neutralization | UAS down or mission-killed | 1 per successful engagement |
| Engagement timeline | Cue-to-fire | ≤ 30 s with pre-cueing |
| Ammunition efficiency | Rockets per kill (hover, trained) | ≤ 2 average |
| Cloud effectiveness | Rotor/motor strike probability | TBD in test |
| Collateral | Downrange BB hazard vs. HE | Lower than HE; not zero |

---

## Measures of Suitability (MOS)

| MOS | Metric | Target |
|-----|--------|--------|
| Carry burden | Launcher + 4 rockets | ≤ 22 kg team load |
| Setup time | Movement to ready | ≤ 30 s |
| Mission-capable rate | Field | ≥ 90% |

---

## Assumptions

1. Two-man team: gunner + ammo bearer.
2. UAS presents IR contrast sufficient for seeker lock.
3. Dispersal fuze functions within notional proximity window.
4. No validated Pk data — all effectiveness bands are analytic placeholders.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [03 — Design Constraints](03-design-constraints.md) | Physical limits |
| [04 — CONOPS / Use Cases](04-conops-use-cases.md) | Employment scenarios |

---

[← Concept Overview](01-concept-overview.md) | [Next: Design Constraints →](03-design-constraints.md)
