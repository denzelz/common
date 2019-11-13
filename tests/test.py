import math
import unittest
from homework import Rectangle


class TestRectangle(unittest.TestCase):
    rectangle_1 = Rectangle(3, 8)
    rectangle_2 = Rectangle(1.4, 4)
    rectangle_3 = Rectangle(4, 4)

    def test_get_rectangle_perimetr(self):
        self.assertEqual(self.rectangle_1.get_rectangle_perimeter(),
                         ((self.rectangle_1.height + self.rectangle_1.width) * 2))
        self.assertEqual(self.rectangle_2.get_rectangle_perimeter(),
                         ((self.rectangle_2.height + self.rectangle_2.width) * 2))

    def test_get_rectangle_square(self):
        self.assertEqual(self.rectangle_1.get_rectangle_square(),
                         self.rectangle_1.height * self.rectangle_1.width)
        self.assertEqual(self.rectangle_2.get_rectangle_square(),
                         self.rectangle_2.height *self.rectangle_2.width)

    def test_get_sum_of_corners_invalid_corners(self):
        for i in range(5, 10):
            with self.assertRaises(ValueError):
                self.rectangle_1.get_sum_of_corners(i)
                self.rectangle_2.get_sum_of_corners(i)

    def test_get_sum_of_corners(self):
        for i in range(1, 5):
            self.assertEqual(self.rectangle_1.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rectangle_2.get_sum_of_corners(i), i * 90)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.rectangle_1.get_rectangle_diagonal(),
                         math.sqrt(math.pow(self.rectangle_1.height, 2) + math.pow(self.rectangle_1.width, 2)))
        self.assertEqual(self.rectangle_2.get_rectangle_diagonal(),
                         math.sqrt(math.pow(self.rectangle_2.height, 2) + math.pow(self.rectangle_2.width, 2)))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rectangle_1.get_radius_of_circumscribed_circle(),
                         self.rectangle_1.get_rectangle_diagonal() / 2)
        self.assertEqual(self.rectangle_2.get_radius_of_circumscribed_circle(),
                         self.rectangle_2.get_rectangle_diagonal() / 2)

    def test_get_radius_of_inscribed_circle_error(self):
        if self.rectangle_1.width != self.rectangle_1.height:
            with self.assertRaises(ValueError):
                self.rectangle_1.get_radius_of_inscribed_circle()

    def test_get_radius_of_inscribed_circle_pass(self):
        self.assertEqual(self.rectangle_3.get_radius_of_inscribed_circle(),
                         self.rectangle_3.get_rectangle_diagonal() / 2 * math.sqrt(2))

    def test_get_radius_of_inscribed_circle_failed(self):
            with self.assertRaises(ValueError):
                self.assertEqual(self.rectangle_1.get_radius_of_inscribed_circle(),
                                 self.rectangle_1.get_rectangle_diagonal() / (2 * math.sqrt(2)))


if __name__ == '__main__':
    unittest.main()
