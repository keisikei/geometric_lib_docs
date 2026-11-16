import math
import unittest
import circle


class CircleTestCase(unittest.TestCase):
    

    def test_area_one(self):						#
        self.assertAlmostEqual(circle.area(1), math.pi)			#
    def test_area_zero(self):						# площадь: area(r) =
        self.assertAlmostEqual(circle.area(0), 0)			# = pi * r^2
    def test_area_two(self):						#
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)		#
    def test_area_float(self):						#
        self.assertAlmostEqual(circle.area(2.5), 6.25 * math.pi)	#


    def test_perimeter_one(self):					#
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)	#
    def test_perimeter_zero(self):					#
        self.assertAlmostEqual(circle.perimeter(0), 0)			# периметр: perimeter(r) 
    def test_perimeter_two(self):					# = 2 * pi * r
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)	#
    def test_perimeter_float(self):					#
        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi)	#


if __name__ == '__main__':
    unittest.main()