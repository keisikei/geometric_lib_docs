import unittest
import triangle


class TriangleTestCase(unittest.TestCase):


    def test_area_normal(self):					#
        self.assertEqual(triangle.area(6, 4), 12)		#
    def test_area_zero_zero_base(self):				#
        self.assertEqual(triangle.area(0, 0), 0)		#
    def test_area_zero_base(self):				# площадь: area(a, h) =
        self.assertEqual(triangle.area(0, 5), 0)		# = a * h / 2
    def test_area_zero_height(self):				#
        self.assertEqual(triangle.area(6, 0), 0)		#
    def test_area_float(self):					#
        self.assertAlmostEqual(triangle.area(2.5, 4), 5.0)	#
    def test_area_float_float(self):				#
        self.assertAlmostEqual(triangle.area(2.5, 2.5), 3.125)	#


    def test_perimeter_normal(self):					#
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)		#
    def test_perimeter_equilateral(self):				# perimeter(a, b, c) =
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)		# = a + b + c
    def test_perimeter_zero_zero_zero(self):				#
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)		#
    def test_perimeter_float(self):					#
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.5, 4), 10.0)	#


if __name__ == '__main__':
    unittest.main()