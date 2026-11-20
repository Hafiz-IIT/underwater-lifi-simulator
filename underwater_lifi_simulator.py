"""Exploratory Beer-Lambert underwater optical-link toy model.

This is not a validated physical link budget: it omits geometric beam spread,
scattering/absorption separation, pointing loss, receiver aperture, ambient
optical noise, bandwidth, and hardware calibration. The OOK BER expression is
an illustrative Gaussian-noise approximation using the module's SNR convention.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import erfc, exp, sqrt, isfinite


def _finite_float(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be finite")
    try:
        normalized = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not isfinite(normalized):
        raise ValueError(f"{name} must be finite")
    return normalized


ATTENUATION_PER_M = {
    "clear": 0.08,
    "coastal": 0.20,
    "turbid": 0.45,
}


@dataclass(frozen=True)
class LinkBudget:
    distance_m: float
    received_power_w: float
    snr_linear: float
    ber_ook: float


def received_power(tx_power_w: float, distance_m: float, attenuation_per_m: float) -> float:
    tx_power_w = _finite_float("tx_power_w", tx_power_w)
    distance_m = _finite_float("distance_m", distance_m)
    attenuation_per_m = _finite_float("attenuation_per_m", attenuation_per_m)
    if min(tx_power_w, distance_m, attenuation_per_m) < 0:
        raise ValueError("physical inputs must be non-negative")
    return tx_power_w * exp(-attenuation_per_m * distance_m)


def ook_ber_from_snr(snr_linear: float) -> float:
    snr_linear = _finite_float("snr", snr_linear)
    if snr_linear < 0:
        raise ValueError("snr must be non-negative")
    return 0.5 * erfc(sqrt(snr_linear / 2.0))


def link_budget(
    *,
    tx_power_w: float,
    distance_m: float,
    water: str = "clear",
    noise_power_w: float = 1e-6,
) -> LinkBudget:
    if water not in ATTENUATION_PER_M:
        raise ValueError("unknown water preset")
    tx_power_w = _finite_float("tx_power_w", tx_power_w)
    distance_m = _finite_float("distance_m", distance_m)
    noise_power_w = _finite_float("noise_power_w", noise_power_w)
    if tx_power_w < 0 or distance_m < 0 or noise_power_w <= 0:
        raise ValueError("transmit power and distance must be non-negative; noise power must be positive")

    rx = received_power(tx_power_w, distance_m, ATTENUATION_PER_M[water])
    snr = rx / noise_power_w
    if not isfinite(snr):
        raise OverflowError("signal-to-noise ratio is outside finite numeric range")
    return LinkBudget(distance_m, rx, snr, ook_ber_from_snr(snr))


def sweep(distances_m: list[float], **kwargs) -> list[LinkBudget]:
    if not isinstance(distances_m, list):
        raise ValueError("distances_m must be a list of finite non-negative numbers")
    normalized = [_finite_float("distance", distance) for distance in distances_m]
    if any(distance < 0 for distance in normalized):
        raise ValueError("distances_m must be non-negative")
    return [link_budget(distance_m=d, **kwargs) for d in normalized]


if __name__ == "__main__":
    for row in sweep([1, 5, 10, 20], tx_power_w=0.01, water="coastal"):
        print(row)
