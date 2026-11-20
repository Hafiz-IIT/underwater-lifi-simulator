from __future__ import annotations
from math import isfinite
from underwater_lifi_simulator import link_budget

def max_distance_for_ber(*, tx_power_w: float, water: str, noise_power_w: float,
                          max_ber: float, search_high_m: float = 200.0,
                          iterations: int = 80) -> float:
    if isinstance(max_ber, bool) or not isinstance(max_ber, (int, float)) or not isfinite(max_ber) or not 0 < max_ber < 0.5:
        raise ValueError("max_ber must be finite and between 0 and 0.5")
    if isinstance(search_high_m, bool) or not isinstance(search_high_m, (int, float)) or not isfinite(search_high_m) or search_high_m <= 0:
        raise ValueError("search_high_m must be finite and positive")
    if isinstance(iterations, bool) or not isinstance(iterations, int) or not 1 <= iterations <= 256:
        raise ValueError("iterations must be an integer between 1 and 256")
    at_zero = link_budget(tx_power_w=tx_power_w, distance_m=0.0, water=water, noise_power_w=noise_power_w)
    if at_zero.ber_ook > max_ber: return 0.0
    at_high = link_budget(tx_power_w=tx_power_w, distance_m=float(search_high_m), water=water, noise_power_w=noise_power_w)
    if at_high.ber_ook <= max_ber: return float(search_high_m)
    low, high = 0.0, float(search_high_m)
    for _ in range(iterations):
        mid = (low + high) / 2.0
        row = link_budget(tx_power_w=tx_power_w, distance_m=mid, water=water, noise_power_w=noise_power_w)
        if row.ber_ook <= max_ber: low = mid
        else: high = mid
    return low
