from __future__ import annotations

from dataclasses import dataclass
from math import erfc, exp, sqrt


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
    if tx_power_w < 0 or distance_m < 0 or attenuation_per_m < 0:
        raise ValueError("physical inputs must be non-negative")
    return tx_power_w * exp(-attenuation_per_m * distance_m)


def ook_ber_from_snr(snr_linear: float) -> float:
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
    if noise_power_w <= 0:
        raise ValueError("noise power must be positive")

    rx = received_power(tx_power_w, distance_m, ATTENUATION_PER_M[water])
    snr = rx / noise_power_w
    return LinkBudget(distance_m, rx, snr, ook_ber_from_snr(snr))


def sweep(distances_m: list[float], **kwargs) -> list[LinkBudget]:
    return [link_budget(distance_m=d, **kwargs) for d in distances_m]


if __name__ == "__main__":
    for row in sweep([1, 5, 10, 20], tx_power_w=0.01, water="coastal"):
        print(row)
