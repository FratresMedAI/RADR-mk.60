# Annex D — Projectile Stabilization

**Document ID:** TKI-30-66 / ANX-D  
**Version:** 0.4.0  
**Status:** Conceptual

Context: [06 — System Description](../docs/06-system-description.md)

---

## Overview

TKI-30-66 fires a **fin-stabilized guided rocket**, not a spin-stabilized kinetic rod. Baseline architecture:

- **Smoothbore launch tube** (notional)
- **Deployable or fixed fins** for flight stability
- **Autopilot** fin control for IR homing maneuvers
- **No sabot discard** — integrated rocket body

Rifled twist for long rods is **not** baseline.

---

## Fin Configuration

| Parameter | Notional |
|-----------|----------|
| Fin count | 4 |
| Span | ~80–100 mm deployed or fixed |
| Control | Autopilot deflection for terminal homing |

---

## Flight Phases

| Phase | Distance | Notes |
|-------|----------|-------|
| Launch | 0 m | Backblast mitigation; seeker may arm post-launch |
| Boost | 0–50 m | Fin authority ramps |
| Midcourse | 50 m – fuze | IR homing |
| Terminal | Fuze actuation | BB dispersal; minimal stability required |

---

## Warhead / CG Considerations

Ti BB payload placed **forward or amidships** per fuze design. CG shift post-dispersal is acceptable — engagement complete.

---

## Failure Modes

| Failure | Effect | Mitigation |
|---------|--------|------------|
| Fin control failure | Miss | Factory autopilot QA |
| Seeker shock | Track loss | Isolation mount |
| Instability pre-dispersal | Fuze error | Aero test |

---

## Open Engineering

- Smoothbore vs. rifled tube for launch — **TBD** (smoothbore preferred for rocket)

---

## Related Documents

- [05 — Key Design Trades](../docs/05-key-design-trades.md)
