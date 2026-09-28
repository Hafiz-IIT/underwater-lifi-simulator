# Architecture

Water attenuation preset + distance + transmit power + noise → Beer-Lambert received power → SNR → approximate OOK BER → distance sweep.

## Invariants
1. Received power must not increase with distance under fixed attenuation.
2. Higher attenuation should reduce received power.
3. Worse SNR should not improve BER.
