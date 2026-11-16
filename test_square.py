import unittest
import square


class SquareTestCase(unittest.TestCase):


    def test_area_normal(self):					#
        self.assertEqual(square.area(5), 25)			#
    def test_area_zero(self):					#
        self.assertEqual(square.area(0), 0)			# площадь: area(a) =
    def test_area_one(self):					# = a * a
        self.assertEqual(square.area(1), 1)			#
    def test_area_float(self):					#
        self.assertAlmostEqual(square.area(2.5), 6.25)		#


    def test_perimeter_normal(self):				#
        self.assertEqual(square.perimeter(5), 20)		#
    def test_perimeter_zero(self):				#
        self.assertEqual(square.perimeter(0), 0)		# периметр: perimeter(a) =
    def test_perimeter_one(self):				# = 4 * a
        self.assertEqual(square.perimeter(1), 4)		#
    def test_perimeter_float(self):				#
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)	#


if __name__ == '__main__':
    unittest.main()