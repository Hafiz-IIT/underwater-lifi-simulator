from __future__ import annotations

from underwater_lifi_simulator import link_budget


def max_distance_for_ber(
    *,
    tx_power_w: float,
    water: str,
    noise_power_w: float,
    max_ber: float,
    search_high_m: float = 200.0,
    iterations: int = 80,
) -> float:
    if not 0 < max_ber < 0.5:
        raise ValueError("max_ber must be between 0 and 0.5")
    if search_high_m <= 0:
        raise ValueError("search_high_m must be positive")

    at_zero = link_budget(
        tx_power_w=tx_power_w,
        distance_m=0.0,
        water=water,
        noise_power_w=noise_power_w,
    )
    if at_zero.ber_ook > max_ber:
        return 0.0

    at_high = link_budget(
        tx_power_w=tx_power_w,
        distance_m=search_high_m,
        water=water,
        noise_power_w=noise_power_w,
    )
    if at_high.ber_ook <= max_ber:
        return search_high_m

    low, high = 0.0, search_high_m
    for _ in range(iterations):
        mid = (low + high) / 2.0
        row = link_budget(
            tx_power_w=tx_power_w,
            distance_m=mid,
            water=water,
            noise_power_w=noise_power_w,
        )
        if row.ber_ook <= max_ber:
            low = mid
        else:
            high = mid

    return low
