# Underwater Li-Fi Simulator

<p align="center"><strong>Underwater Optical Link Modeling</strong><br/><sub>Attenuation → received power → SNR → approximate OOK BER → range.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-reproducible%20prototype-blue" alt="Prototype"/> <img src="https://img.shields.io/badge/domain-underwater%20optical%20communications-purple" alt="Optical communications"/></p>

## Question

**How does water condition and distance constrain a simplified underwater optical communication link?**

```
Water condition + distance + Tx power + noise
                     ↓
             attenuation model
                     ↓
              received power
                     ↓
                    SNR
                     ↓
             approximate OOK BER
                     ↓
               usable range
```

## Try it

```bash
python underwater_lifi_simulator.py
python range_analysis.py
python -m unittest discover -s tests -v
```

`range_analysis.py` adds BER-constrained maximum-distance estimation using a bounded search.

## Implemented

- water-condition presets
- Beer–Lambert attenuation
- received optical power
- SNR
- approximate OOK BER
- distance sweeps
- BER-constrained range analysis
- deterministic CI

## Research boundary

This is a **simplified software model**. It is not a validated underwater modem design, hardware implementation, or field measurement.

## Why it is in the portfolio

The project connects an early communications concept to an executable quantitative model: assumptions become parameters, parameters become sweeps, and the resulting claims remain inspectable.

Related: [Logistics Optimization Lab](https://github.com/Hafiz-IIT/logistics-optimization-lab)
