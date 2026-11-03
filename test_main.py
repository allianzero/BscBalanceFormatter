"""Tests for BscBalanceFormatter."""
import unittest
from main import calculate


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertAlmostEqual(calculate(1500000000000000000), 1.5, places=6)


if __name__ == "__main__":
    unittest.main()
