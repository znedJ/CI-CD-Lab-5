import unittest
def triangle_area(a, h):
    if a < 0 or h < 0:
        raise ValueError("Основание и высота должны быть неотрицательными.")
    return (a * h) / 2
def triangle_perimetr(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны должны быть неотрицательными.")
    return a + b + c
class TestTriangleArea(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(triangle_area(4, 5), 10)
        self.assertEqual(triangle_area(10, 2), 10)
        self.assertEqual(triangle_area(3, 6), 9)

    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(4, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)



class TestTrianglePerimetr(unittest.TestCase):

    def test_perimetr_positive(self):
        self.assertEqual(triangle_perimetr(4, 5, 3), 12)
        self.assertEqual(triangle_perimetr(10, 2, 8), 20)
        self.assertEqual(triangle_perimetr(3, 6, 4), 13)

    def test_perimetr_zero(self):
        self.assertEqual(triangle_perimetr(0, 0, 0 ), 0)


if __name__ == '__main__':
    unittest.main()
