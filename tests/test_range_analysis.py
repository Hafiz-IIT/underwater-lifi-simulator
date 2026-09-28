import unittest

from range_analysis import max_distance_for_ber


class RangeAnalysisTests(unittest.TestCase):
    def test_clear_water_supports_longer_range_than_turbid(self):
        kwargs = dict(tx_power_w=0.0001, noise_power_w=1e-5, max_ber=0.1)
        clear = max_distance_for_ber(water="clear", **kwargs)
        turbid = max_distance_for_ber(water="turbid", **kwargs)
        self.assertGreater(clear, turbid)

    def test_invalid_ber_threshold(self):
        with self.assertRaises(ValueError):
            max_distance_for_ber(
                tx_power_w=1,
                water="clear",
                noise_power_w=1,
                max_ber=0.6,
            )


if __name__ == "__main__":
    unittest.main()
