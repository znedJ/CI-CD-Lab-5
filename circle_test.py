import unittest
def circle_area(r):
    if r < 0 :
        raise ValueError("Радиус должен быть неотрицательным.")
    return (3,14 * r * r)
def circle_perimetr(r):
    if r < 0:
        raise ValueError("Радиус должен быть неотрицательным.")
    return 6,28 * r
class TestTriangleArea(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(circle_area(4), 50,24)
        self.assertEqual(circle_area(10), 314)


    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)


class TestTrianglePerimetr(unittest.TestCase):

    def test_perimetr_positive(self):
        self.assertEqual(circle_perimetr(100), 628)
        self.assertEqual(circle_perimetr(3), 18,84)

    def test_perimetr_zero(self):
        self.assertEqual(circle_perimetr(0), 0)


if __name__ == '__main__':
    unittest.main()
