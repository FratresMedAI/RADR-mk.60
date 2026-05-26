# 02 — Operational Requirements

**Document ID:** RADR / DOC-02  
**Version:** 1.7.0  
**Status:** Conceptual

Annex B: [KPP Targets](../annexes/B-kpp-targets.md)

---

## Primary Mission

Provide **squad and SOF** a **mid-range drone destroyer** — defeat **Group 1–2 UAS** from **200 m** minimum through **1200 m** maximum (**800–1200 m** primary band; **1000 m** design sweet spot) using a **speed-first** guided flak rocket with **one-person reload**.

---

## Threat Requirements

The system shall be designed to engage:

| ID | Threat | Priority |
|----|--------|----------|
| TH-01 | FPV kamikaze drones | High |
| TH-02 | Small-to-medium quadcopters | High |
| TH-03 | Loitering munitions | High |
| TH-04 | Terrain-matching / GPS-denied gliding UAS (Hornet / “Martian” class) | High |
| TH-05 | Other Group 1–2 UAS in swarm / interdiction roles | High |

**Out of threat set:** Group 3+ UAS, fixed-wing aircraft, armored ground targets.

---

## Range envelope (locked)

| | Range | Notes |
|---|-------|-------|
| **Minimum** | **200 m** | Not closer — compressed seeker lock, **boost-phase** shot (~1.6 s TOF @ 200 m), proximity fuze needs flight path to **~20 ft** standoff |
| **Primary band** | **800–1200 m** | Mid-range vs. MG/SAM gap |
| **Sweet spot** | **1000 m** | Motor/velocity design anchor (**330–350 m/s**) |
| **Maximum** | **1200 m** | Envelope (~332 m/s, ~4.7 s TOF) |

**200–800 m** is valid close-in employment; **800 m** is the lower edge of the primary band, not the minimum engagement distance.

---

## Locked KPPs

| Parameter | Threshold | Objective |
|-----------|-----------|-----------|
| Caliber | 60 mm | Locked |
| Rocket OAL | 457 mm (18 in) | Locked |
| Rocket mass | ≤ 3.5 kg | Locked |
| Launcher OAL | 1016 mm (40 in) | Locked |
| Launcher mass (empty) | ≤ 5.5 kg | Locked |
| System mass (launcher + 1 round) | ≤ 9.0 kg | Locked |
| Warhead | 300 × 7 mm dense alloy rough-edged cubes | Locked |
| Dispersal | Pyrotechnic charge; forward cone @ ~20 ft | ~10–12 ft wide |
| Fuze | Radar or mm-wave proximity + timed backup | Locked |
| Seeker | 100 mm IR F&F | Lock before launch |
| Guidance | **Moderate-maneuver** nose canards | Not high OBA |
| Fins | 4 spring-loaded swept; **mechanical lock** when deployed | Deploy on exit |
| Motor | Evolution Space propellant; **mildly progressive** burn (**750–850 N** first **1–2 s**, ramp to **1050–1150 N**); **2950–3050 N·s**; **~3.3 s** | Locked |
| Range (min) | **≥ 200 m** | Locked |
| Range (band) | **800–1200 m** employment | Locked |
| Range (sweet spot) | **1000 m** | **330–350 m/s** calibrated here |
| Range (max) | **1200 m** | Locked envelope |
| Backblast | ≤ 10 yd (30 ft) | Locked |
| Tube | **Tank-shell** alloy/composite tube; pop top → load → unscrew bottom in bore | Locked |
| Breech | Gustav flip + positive lock | Locked |
| Controls | Dual-trigger + lock tone; **front** = seeker/tone, **rear** = fire | Locked |
| Sight | **Digital cam sight**; **smooth 1×–20×**; **+ / −** on foregrip; fold-out display | Locked |
| Sighting | **RPG-style shouldering**; display at arm’s length; **no cheek weld** | Locked |
| CoG | Rear-biased | Locked |
| Rocket retention stop | Engaged when not armed; releases per interlock table | Locked |
| One-person reload | Required | — |
| Cost per rocket | ≤ $500 | ≤ $300 |

---

## Safety Requirements

| ID | Requirement | Verification (concept) |
|----|-------------|--------------------------|
| SAF-01 | Rocket shall not slide forward in bore during carry/sling unless retention stop is intentionally released | Mechanical stop + logic |
| SAF-02 | Retention stop shall disengage only when breech fully closed **and** front trigger held **and** seeker ready tone active | Interlock table — Annex F |
| SAF-03 | Retention stop shall re-engage when front trigger is released | Annex F |
| SAF-04 | Rear trigger shall not initiate launch without lock tone | Annex F |
| SAF-05 | Seeker shall not arm until tube seated (pressure + contacts) | Annex F |
| SAF-06 | Backblast danger zone ≤ 10 yd (30 ft) — cleared before fire and breech open | Locked |

---

## Employment Sequence (Required)

| Step | Gunner action | System response |
|------|---------------|-----------------|
| 1 | Open breech (pull spring bolt, swing open) | Rear trigger disabled; retention stop **engaged** |
| 2 | Pop top (PULL) on tube | Top open |
| 3 | Slide tube into bore | Tube seated |
| 4 | Unscrew bottom cap in bore | Rocket exposed in tube |
| 5 | Close breech | **Rocket ready** (continuity) |
| 6 | Hold front trigger | Seeker on; tone at lock; retention stop **disengages** |
| 7 | Pull rear trigger (front held) | Rocket flies free |
| 8 | Open breech after safe interval | Spent tube drops |

**Authoritative interlocks:** [Annex F](../annexes/F-employment-and-breech.md) — [Gunner sequence](../annexes/F-employment-and-breech.md#loading-and-firing--gunners-sequence) · [Retention stop](../annexes/F-employment-and-breech.md#rocket-retention-stop) · [Breech](../annexes/F-employment-and-breech.md#breech-mechanism)

---

## MOEs (Notional)

| MOE | Target |
|-----|--------|
| Mission kill vs. TH-01–TH-05 at 1000 m | TBD live fire |
| Fuze function (proximity primary or timed backup) | ≥ 99% |
| Time threat → fire | Minimize |
| Rockets per kill (hover quadcopter) | ≤ 2 (trained) |
| One-person carry/reload | ≤ 9.0 kg system |

---

## Assumptions

- Gunner can rough-aim within seeker FOV  
- Progressive motor achieves **~330–350 m/s** class closure at **1000 m** (locked baseline)
- Radar or mm-wave proximity + timed backup covers fuze reliability for forward-cone geometry at ~20 ft  

---

[← Concept Overview](01-concept-overview.md) | [Next: Design Constraints →](03-design-constraints.md)
