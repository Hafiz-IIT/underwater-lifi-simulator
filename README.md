# Underwater Li-Fi Simulator

A reproducible software model inspired by my earlier underwater optical/Li-Fi science-exhibition work.

## Implemented
- Beer-Lambert attenuation
- water-condition presets
- received optical power
- signal-to-noise ratio
- approximate OOK bit-error rate
- distance sweep helper
- deterministic tests

## Run
```bash
python -m unittest discover -s tests -v
python underwater_lifi_simulator.py
```

## Boundary
This is a simplified simulator, not a claim of new hardware, field measurements, modem implementation, or validated ocean-channel performance.
