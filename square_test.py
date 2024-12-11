import unittest


class SquareTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_area_1(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_circle_area_2(self):
        res = area(7 * 5)
        self.assertEqual(res, 35 ** 2)

    def test_circle_perimeter_1(self):
        res = perimeter(8 * 15)
        self.assertEqual(res, (8 * 15) * 4)

    def test_circle_perimeter_2(self):
        res = perimeter(45)
        self.assertEqual(res, 45 * 4)


def area(a):
    return a * a


def perimeter(a):
    return 4 * a

