# 07 — Limitations and Risks

**Document ID:** TKI-30-66 / DOC-07  
**Version:** 0.4.0  
**Status:** Conceptual

---

## Purpose

Honest assessment of capability limits and risks for the **Ti BB flak / onboard IR** configuration.

---

## Capability Limitations

### Range and Target Set

| Limitation | Detail |
|------------|--------|
| Not long-range | Design 150–600 m; drop-off beyond 800 m |
| High-altitude UAS | Poor engagement above ~500 m AGL |
| Fast crossing targets | Low Pk; cloud may miss narrow window |
| Large UAS (> 25 kg) | Insufficient BB density at range |
| Swarms | One rocket per engagement cycle |

### Guidance and Environment

| Limitation | Detail |
|------------|--------|
| IR lock required | No lock = should not fire |
| Low-thermal UAS | Difficult seeker acquisition |
| Not all-weather | Rain/fog/smoke degrade IR |
| IR countermeasures | Flares may seduce simplified seeker |
| Not full Stinger class | Smaller seeker, lower discrimination |

### Warhead / Flak

| Limitation | Detail |
|------------|--------|
| Dispersal timing | Early/late fuze = miss |
| Wind | Shifts BB cloud |
| BB velocity at range | Reduced lethality vs. muzzle |
| No penetrator | Hardened UAS may survive sparse hits |
| Collateral | BBs downrange — ROE risk in urban areas |
| Proximity dependence | Unlike rod, needs reasonable fuze solution |

### Physical

| Limitation | Detail |
|------------|--------|
| Backblast | No enclosed firing |
| Dud rocket | Seeker or fuze failure wastes round |

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| R-01 | Premature dispersal | Low | High (miss) | Fuze test program |
| R-02 | Late / no dispersal | Low | High (miss) | Factory fuze QA |
| R-03 | Seeker break-lock | Medium | Medium | Drone-optimized algorithms |
| R-04 | IR flares / CCM | Medium | Medium | Filtering; short TOF |
| R-05 | Obscuration | Medium | Medium | Layered defense |
| R-06 | Backblast injury | Medium | High | Training; SOP |
| R-07 | Swarm saturation | High | High | Multiple teams; EW |
| R-08 | BB collateral | Medium | Medium | ROE; sector discipline |
| R-09 | Cold-target lock fail | Medium | Medium | Training; visual ID |
| R-10 | Cost per kill | Medium | Low | Volume procurement |

---

## Countermeasure Vulnerability

| Countermeasure | Effect | Severity |
|----------------|--------|----------|
| IR flares | Seeker seduction | Moderate |
| Smoke / obscurants | Blocks IR | High |
| Low-thermal airframe | Hard lock | Moderate |
| Laser warning | N/A (no laser) | None |
| Swarm | Ammo exhaustion | High |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [05 — Key Design Trades](05-key-design-trades.md) | Design rationale |
| [08 — Layered Defense Integration](08-layered-defense-integration.md) | Layer context |

---

[← System Description](06-system-description.md) | [Next: Layered Defense Integration →](08-layered-defense-integration.md)
