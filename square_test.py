import unittest
def square_area(a):
    if a < 0:
        raise ValueError("Сторон должна быть неотрицательной.")
    return a*a
def square_perimetr(a):
    if a < 0:
        raise ValueError("Сторон должна быть неотрицательной.")
    return a*4
class TestTriangleArea(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(10), 100)

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)




class TestTrianglePerimetr(unittest.TestCase):

    def test_perimetr_positive(self):
        self.assertEqual(square_perimetr(4), 16)
        self.assertEqual(square_perimetr(10), 40)

    def test_perimetr_zero(self):
        self.assertEqual(square_perimetr(0 ), 0)


if __name__ == '__main__':
    unittest.main()
