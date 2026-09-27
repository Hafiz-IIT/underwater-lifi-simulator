import unittest

from underwater_lifi_simulator import link_budget, received_power


class UnderwaterLiFiTests(unittest.TestCase):
    def test_power_decreases_with_distance(self):
        near = received_power(1.0, 1.0, 0.2)
        far = received_power(1.0, 10.0, 0.2)
        self.assertGreater(near, far)

    def test_turbid_water_has_lower_received_power(self):
        clear = link_budget(tx_power_w=0.01, distance_m=10, water="clear")
        turbid = link_budget(tx_power_w=0.01, distance_m=10, water="turbid")
        self.assertGreater(clear.received_power_w, turbid.received_power_w)

    def test_worse_channel_increases_ber(self):
        clear = link_budget(tx_power_w=0.0001, distance_m=10, water="clear", noise_power_w=1e-5)
        turbid = link_budget(tx_power_w=0.0001, distance_m=10, water="turbid", noise_power_w=1e-5)
        self.assertLess(clear.ber_ook, turbid.ber_ook)


if __name__ == "__main__":
    unittest.main()
