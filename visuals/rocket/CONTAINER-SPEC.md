# RADR mk.60 — Protective tube + rocket interface (CAD design spec)

**Status:** **Locked** — official concept/plan. Visual render unchanged: [`output/radr-container-authoritative.png`](output/radr-container-authoritative.png).

Not procurement authority. Employment: [Annex F § Loading sequence](../../annexes/F-employment-and-breech.md#loading-and-firing--gunners-sequence). Rocket body: [`ROUND-SPEC.md`](ROUND-SPEC.md).

---

## Overall philosophy (tank shell)

- **Protective tube stays in the launcher** through load, arm, and fire; spent tube ejects when the breech opens after the shot.
- **Rocket OD < tube ID** — clearance on all sides; rocket **flies free** from the tube once the **retention stop** releases (minimal launch resistance).
- **KISS:** fast load (under **10 s** for a trained soldier), few parts, no tools.

---

## Authoritative art (unchanged)

| Asset | Role |
|-------|------|
| [`input/radr-container-paint-schematic.png`](input/radr-container-paint-schematic.png) | User Paint (side + top **PULL**) |
| [`output/radr-container-authoritative.png`](output/radr-container-authoritative.png) | **Locked** polished render — do not regenerate for spec text updates |

**Side view (horizontal, left → right):** **left = top** (pop-top / **PULL**) · **right = breech** (hand screw cap).

---

## Protective tube (CAD)

| Requirement | Spec |
|-------------|------|
| **Material** | Lightweight **alloy or composite**, camouflage finish |
| **Length** | Rocket OAL + **small margin** (~18 in class round) |
| **Internal diameter** | **Larger than rocket OD** — radial clearance all around |
| **Top** | **Red pull tab** — quick open; stencil **PULL** |
| **Bottom (breech end)** | **Screw-off cover** — hand removal **with gloves**; no tools |
| **Internal features** | Minimal **foil or contact points** for **electrical continuity** with seated rocket |
| **External marking** | **RADR mk.60** in white (matches art) |
| **Aft rim** | Shoulder step — breech sealing face + **retention stop** contact on tube (not on bare rocket) |

---

## Rocket inside tube (interface)

| Requirement | Spec |
|-------------|------|
| **Outer diameter** | **Smaller than tube ID** — no bind; no significant launch drag |
| **Electrical** | Light **wiring / foil contacts** mate tube contacts when properly seated |
| **Retention** | Launcher **mechanical retention stop** bears on **tube aft shoulder** until arm interlock |
| **Launch** | Rocket exits tube freely after stop release; tube remains until post-fire eject |

Detail: [`ROUND-SPEC.md`](ROUND-SPEC.md).

---

## Loading sequence (locked)

After **open breech** (clear spent tube):

| Step | Gunner | System |
|------|--------|--------|
| 1 | **Pull** red tab; **open top** of tube | Top open; bottom cap still on |
| 2 | **Slide** entire tube into launcher bore | Tube in bore; breech open |
| 3 | **Unscrew** bottom cover of tube (in bore) | Breech end open; rocket exposed in tube |
| 4 | **Close** breech (deadbolt snap) | `LOCKED_SEATED` |
| 5 | — | **Electrical continuity** → **rocket ready** (seat confirm + rim/foil contacts) |
| 6 | **Front trigger** + **steady lock tone** | Retention stop **releases** |
| 7 | **Rear trigger** (front held) | Rocket **flies free**; recoilless vent |

**Constraints:** under **10 s** load for trained soldier; minimize parts; continuity must not add meaningful launch resistance.

---

## Do not change in art passes

- Two-closure layout (pop top + screw bottom).  
- Left = top / right = breech in horizontal side view.  
- **PULL** tab and **RADR mk.60** stencil.  
- Launcher palette family ([stowed launcher](../launcher/output/radr-bazooka-authoritative-stowed.png)).
