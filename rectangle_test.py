import unittest
def rectangle_area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны должны быть неотрицательными.")
    return (a * b)
def rectangle_perimetr(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны должны быть неотрицательными.")
    return (a + b)*2
class TestTriangleArea(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(rectangle_area(4, 5), 20)
        self.assertEqual(rectangle_area(10, 2), 20)
        self.assertEqual(rectangle_area(3, 6), 18)

    def test_area_zero(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(4, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)


class TestTrianglePerimetr(unittest.TestCase):

    def test_perimetr_positive(self):
        self.assertEqual(rectangle_perimetr(4, 5), 18)
        self.assertEqual(rectangle_perimetr(3, 6), 18)
        self.assertEqual(rectangle_perimetr(10, 2), 24)

    def test_perimetr_zero(self):
        self.assertEqual(rectangle_perimetr(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
