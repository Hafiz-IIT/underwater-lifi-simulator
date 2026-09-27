# Underwater Li-Fi Simulator

> **A reproducible optical-channel baseline for the underwater Li-Fi idea: attenuation, link budget, SNR, BER, and turbidity.**

Underwater optical communication was one of the older science/research ideas, but a credible public artifact should distinguish a software channel model from hardware experimentation. This repository implements the former and states that boundary explicitly.

## Implemented
- Beer-Lambert optical attenuation
- clear/coastal/turbid attenuation presets
- received optical-power calculation
- SNR calculation
- approximate OOK BER
- distance sweep helper
- input validation

## Run
```bash
python -m unittest discover -s tests -v
python underwater_lifi_simulator.py
```

## Repository map
- `underwater_lifi_simulator.py` — core implementation
- `tests/` — deterministic tests
- `examples/` — reproducible example
- `docs/architecture.md` — architecture
- `docs/research-agenda.md` — experiments and research lineage
- `STATUS.md` — claims boundary
- `CITATION.cff` — citation metadata

## Pipeline
**transmit power → water attenuation → distance → received power → noise → SNR → OOK BER**

## Research lineage
This repository is the concrete software artifact for the historical Underwater Li-Fi / optical data-transmission work and is separate from the broader 6G/solar-fiber and wireless-power concepts that still remain research backlog.

## Evaluation direction
Sweep distance, water attenuation, transmit power, and noise floor; create link-budget curves and sensitivity analysis. Hardware claims require separate instrumentation and experimental records.

## Maturity
**Research prototype.** This is a simplified analytical simulator. It does not claim a built modem, underwater field tests, hardware innovation, validated ocean optics, or measured throughput.
