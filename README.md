# Underwater Li-Fi Simulator

> Simplified underwater optical-communication simulator covering attenuation, received power, SNR and OOK bit-error rate.

## Status
**Reproducible prototype** with executable code, tests, CI, architecture, evaluation and roadmap documentation.

## Problem
Underwater optical links trade range against attenuation, turbidity, transmit power and noise. A transparent software model provides a defensible bridge from earlier Li-Fi concepts to measurable experiments.

## Architecture
Water attenuation preset + distance + transmit power + noise → Beer-Lambert received power → SNR → approximate OOK BER → distance sweep.

## Run
```bash
python -m unittest discover -s tests -v
python underwater_lifi_simulator.py
```

## Implemented
- Water-condition presets
- Beer-Lambert attenuation
- Received optical power
- SNR calculation
- Approximate OOK BER
- Distance sweep helper
- Tests and CI

## Research lineage
- *AI in Energy Efficiency Management*
- *Smart Urban Infrastructures: AI-Enabled City Optimization*
- *Bridging Classical Control and Modern AI: A Unified Framework for Automated Agents*

## Evaluation
Tests verify monotonic power loss with distance, worse turbid-water performance and BER degradation under poorer channels.

## Limitations
- Simplified channel model
- No scattering/geometric optics model
- No real hardware measurements
- No modem/PHY implementation
- No ocean validation claim

## License
MIT.
