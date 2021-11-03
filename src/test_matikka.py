import unittest
from matikka import ympyran_ala
from math import pi

class TestMatikka(unittest.TestCase):
    def test_ala(self):
        self.assertAlmostEqual(ympyran_ala(0),0)
        self.assertAlmostEqual(ympyran_ala(1),pi)
        self.assertAlmostEqual(ympyran_ala(2.5), pi*2.5**2)

    def test_values(self):
        self.assertRaises(ValueError, ympyran_ala, -2.5)

    def test_types(self):
        self.assertRaises(TypeError, ympyran_ala, "säde")
        self.assertRaises(TypeError, ympyran_ala, True)


if __name__ == '__main__':
    unittest.main()