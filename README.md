# Weapon Simulator

A command-line FPS weapon mechanics simulator written in Python. Pick a weapon, fire it, and watch ammo, fire rate and recoil behave the way they would in a shooter game.

## Features

- **8 weapons in 3 categories:** pistols (Glock 17, Desert Eagle, Revolver), assault rifles (M4, AK47, SCAR) and snipers (Barrett .50, Hunting Rifle)
- **Recoil patterns:** each weapon has its own repeating kick pattern, plus a small random jitter on every shot, so no two sprays are identical
- **Time-based recoil recovery:** recoil decays exponentially between shots with a half-life of 1 second, so spraying builds recoil and pausing lets it settle
- **Fire rate limits:** shooting faster than a weapon's fire rate is blocked
- **Ammo and reloading:** each weapon has its own magazine size and reload time

## Design

The weapons are built with **inheritance**. A base `Weapons` class holds the shared behaviour (shooting, reloading, recoil), category classes (`Pistol`, `AR`, `Sniper`) group the weapons, and each specific weapon only defines its own stats:

```
Weapons
├── Pistol  → Glock17, Deagle, Revolver
├── AR      → M4, AK47, Scar
└── Sniper  → Barrett50, HuntingRifle
```

Adding a new weapon means writing one small class with its stats. No shooting or recoil code needs to change.

## Getting started

Requires **Python 3.10+** (uses `match` statements). No external packages are needed.

```bash
git clone https://github.com/Faisal1506/weapon-simulator.git
cd weapon-simulator
python weapon_sim.py
```

## Example

An M4 spray, then a 3-second pause before the last shot:

```
Ammo: 29 | Recoil X: -0.02, Y: 0.16
Ammo: 28 | Recoil X: -0.02, Y: 0.36
Ammo: 27 | Recoil X: 0.00, Y: 0.49
Ammo: 26 | Recoil X: -0.02, Y: 0.67
Ammo: 25 | Recoil X: 0.01, Y: 0.80
Ammo: 24 | Recoil X: 0.00, Y: 0.30
```

## Planned improvements

- Per-weapon jitter, so snipers are steadier and ARs are more random
- Longer spray patterns for assault rifles
