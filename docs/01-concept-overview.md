# 01 — Concept Overview

**Document ID:** TKI-30-66 / DOC-01  
**Version:** 0.4.0  
**Status:** Conceptual

---

## Purpose

TKI-30-66 (internal codename: **Splash**) is a conceptual shoulder-fired weapon system that gives squad- and SOF-level units a lightweight, terminal-layer defeat capability against small-to-medium unmanned aircraft systems (UAS).

The system fills the gap when higher-echelon counter-UAS assets are saturated, unavailable, jammed, or overkill for the threat: a **guided flak rocket** that is man-portable, relatively cheap per shot, and simple to employ.

---

## Problem Statement

Squad and SOF elements face close-in UAS threats — ISR platforms, FPV attackers, and loitering munitions — without always having vehicle SHORAD, EW, or missile interceptors at hand. Small arms are cheap but ineffective against maneuvering drones; missiles are effective but heavy, expensive, and scarce.

TKI-30-66 proposes a middle path: a **reusable Gustav-like launcher** firing **lightweight IR-guided rockets** with a **titanium BB flak** warhead.

---

## Core Concept

### Launcher

A reusable, shoulder-fired, recoilless-style launcher with **flip-open breech** reloading — operationally similar to Carl Gustaf, scaled to the **40–66 mm class** (50 mm nominal baseline). The launcher is the tube and sight; it does **not** house a tracking radar or laser designator.

### Rocket

A lightweight guided rocket, **up to ~457 mm (18 in / 1.5 ft)** overall length, kept as light as practicable (~2.3 kg goal). Components:

- Propulsion with low-to-moderate backblast mitigation
- **Onboard IR seeker** — fire-and-forget, baby Stinger / Igla style, optimized for drone thermal signatures
- **Ti BB flak warhead** — disperses a cloud of titanium ball bearings near the target (rocket-delivered flak)
- Fin stabilization (conventional rocket)

### Guidance

**Onboard fire-and-forget IR homing.** The gunner acquires the target, achieves seeker lock, and fires. The rocket tracks autonomously. **No laser beam-riding.** No separate designator operator.

### Warhead / Kill Mechanism

Near the target, the rocket releases a **dispersed cloud of Ti BBs** intended to strike rotors, motors, wings, or airframe — flak-style defeat rather than a single kinetic penetrator. Defeat is by **coverage and fragment strike**, not rod impact.

### Stabilization

Fin-stabilized rocket flight. See [Annex D — Projectile Stabilization](../annexes/D-projectile-stabilization.md).

---

## Design Philosophy

| Principle | Application |
|-----------|-------------|
| **KISS** | One rocket SKU; onboard seeker; mechanical dispersal; no external designator |
| **Lightweight** | Minimum rocket mass; launcher without heavy fire-control module |
| **Man-portable** | Launcher ~7 kg; 2-man team carries launcher + multiple rockets |
| **Cheap per shot** | Target ~$200–400/round at volume vs. missiles |
| **Low backblast** | Safer than full Gustaf class for routine squad use |
| **Honest capability** | Terminal, close-in; not Stinger replacement; not all-weather |

---

## What TKI-30-66 Is

- A terminal **flak rocket** for Group 1–2 UAS at 150–600 m (800 m aspirational under favorable conditions)
- A squad/SOF organic asset with fire-and-forget employment
- A complement to layered C-UAS — not a replacement for SHORAD, EW, or Coyote-class interceptors

## What TKI-30-66 Is Not

- A kinetic rod or long-rod penetrator system
- A laser-designated or beam-riding weapon
- A full Stinger / Igla equivalent (seeker and warhead are deliberately smaller and simpler)
- A long-range or all-weather area-defense system
- A validated, fielded, or procurement-ready system

---

## Internal Codename

**Splash** is used informally within this project. It is not a program of record designation.

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [02 — Operational Requirements](02-operational-requirements.md) | KPPs and MOEs |
| [06 — System Description](06-system-description.md) | Hardware overview |
| [07 — Limitations and Risks](07-limitations-and-risks.md) | Capability ceiling |

---

[Next: Operational Requirements →](02-operational-requirements.md)
