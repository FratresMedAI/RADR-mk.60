# 07 — Limitations and Risks

**Document ID:** RADR / DOC-07  
**Version:** 0.7.0  
**Status:** Conceptual

---

## Limitations

| Limit | Detail |
|-------|--------|
| **Not high off-boresight** | Gunner must point roughly at target |
| **Low-maneuver** | Large initial aim errors may not be recoverable |
| **1000 m range** | **Goal** — motor trajectory not yet proven |
| **Fuze geometry** | Early/late actuation degrades **~20 ft** cone |
| **IR environment** | Smoke, rain, decoys affect lock tone reliability |
| **Crossing targets** | Lower Pk than hover |
| **Backblast** | **10 yd (30 ft)** still lethal if ignored |
| **Collateral** | Cubes continue downrange — ROE required |
| **Not Stinger** | Shorter envelope, simpler seeker |
| **Concept only** | No fielded hardware |

---

## Risks

| ID | Risk | Mitigation |
|----|------|------------|
| R-01 | Motor underperforms vs. 1000 m | Ballistic test; grain iteration |
| R-02 | Progressive grain / backblast coupling | Thrust-time test in 10 yd SOP |
| R-03 | Proximity fuze failure | **Timed backup**; factory QA |
| R-04 | Seeker lock failures | Training; holographic aim cues |
| R-05 | Spring fin fail-to-deploy | Mechanical QA |
| R-06 | Breech lock / seating false state | Deadbolt QC; gunner drills |
| R-07 | Cube lethality unproven at range | Live fire vs. representative UAS |
| R-08 | Sight/thermal cost overrun | Phased sight roadmap |

---

[← System Description](06-system-description.md) | [Next: Layered Defense →](08-layered-defense-integration.md)
