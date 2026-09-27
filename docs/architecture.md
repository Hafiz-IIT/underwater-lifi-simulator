# Architecture

```mermaid
flowchart LR
    N0[transmit power] --> N1
    N1[water attenuation] --> N2
    N2[distance] --> N3
    N3[received power] --> N4
    N4[noise] --> N5
    N5[SNR] --> N6
    N6[OOK BER]
```

## Channel preset
Water condition maps to an attenuation coefficient.

## Attenuation
Beer-Lambert decay converts transmit power to received optical power.

## Noise model
Received power is compared with a configurable noise floor.

## Link metric
SNR feeds an approximate OOK bit-error-rate expression.

## Sweep
Multiple distances generate a reproducible link-budget curve.

## Design principle
A simulation should expose its physical assumptions so later hardware results can be compared against them rather than retrofitted.
