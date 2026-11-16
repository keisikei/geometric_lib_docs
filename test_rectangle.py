import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):

    
    def test_area_normal(self):						#
        self.assertEqual(rectangle.area(3, 4), 12)			#
    def test_area_zero_side(self):					#
        self.assertEqual(rectangle.area(10, 0), 0)			# 
    def test_area_zero_zero(self):					#
        self.assertEqual(rectangle.area(0, 0), 0)			# площадь: area(a, b) =
    def test_area_equal_sides(self):					# a * b
        self.assertEqual(rectangle.area(10, 10), 100) 			#
    def test_area_float(self):						#
        self.assertAlmostEqual(rectangle.area(2.5, 4), 10.0) 		#
    def test_area_float_float(self):					#
        self.assertAlmostEqual(rectangle.area(2.5, 2.5), 6.25) 		#


    def test_perimeter_normal(self):					#
        self.assertEqual(rectangle.perimeter(3, 4), 14)			#
    def test_perimeter_zero_side(self):					#
        self.assertEqual(rectangle.perimeter(10, 0), 20)		# 
    def test_perimeter_zero_zero_side(self):				# perimeter(a, b) =
        self.assertEqual(rectangle.perimeter(0, 0), 0)			# 2 * (a + b)
    def test_perimeter_equal_sides(self):				# 
        self.assertEqual(rectangle.perimeter(10, 10), 40)		#
    def test_perimeter_float_float(self):				#
        self.assertAlmostEqual(rectangle.perimeter(2.5, 1.5), 8.0)	#
    def test_perimeter_float(self):					#
        self.assertAlmostEqual(rectangle.perimeter(2.5, 2), 9.0)	#


if __name__ == '__main__':
    unittest.main()