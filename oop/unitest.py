from oop.homework import Cat, Wall
import unittest

class TestCat(unittest.TestCase):


    # def test_set_average_speed(self):
    #     cat_1 = Cat(1)
    #     cat_1._set_average_speed(50)
    #     self.assertEqual(50, cat_1.average_speed)

    def test_saturation_level(self):
        self.assertEqual(Cat.saturation_level, 50)

    def test_increase_saturation_level(self):
        cat_1 = Cat(1)
        cat_1._increase_saturation_level(50)
        self.assertEqual(cat_1.saturation_level, 100)

    def test_reduce_saturation_level(self):
        cat_1 = Cat(1)
        cat_1._reduce_saturation_level(40)
        self.assertEqual(cat_1.saturation_level, 10)

    def test_increase_saturation_level_limit(self):
        cat_1 = Cat(1)
        cat_1._increase_saturation_level(100)
        self.assertEqual(cat_1.saturation_level, 100)

    def test_reduce_saturation_level_limit(self):
        cat_1 = Cat(1)
        cat_1._reduce_saturation_level(100)
        self.assertEqual(cat_1.saturation_level, 0)

    def test_eat_fodder(self):
        cat_1 = Cat(1)
        cat_1.eat('fodder')
        self.assertEqual(cat_1.saturation_level, 60)
        cat_2 = Cat(1)
        cat_2.eat('apple')
        self.assertEqual(cat_2.saturation_level, 55)
        cat_3 = Cat(1)
        cat_3.eat('milk')
        self.assertEqual(cat_3.saturation_level, 52)

    def test_set_average_speed_for_age_6(self):
        cat_1 = Cat(6)
        cat_2 = Cat(9)
        cat_3 = Cat(12)
        self.assertEqual(cat_1.average_speed, 12)
        self.assertEqual(cat_2.average_speed, 9)
        self.assertEqual(cat_3.average_speed, 6)

    def test_run(self):
        cat_1 = Cat(6)
        cat_1.run(4)
        cat_2 = Cat(9)
        cat_2.run(7)
        self.assertEqual(cat_1.saturation_level, 45)
        self.assertEqual(cat_2.saturation_level, 35)

    # def test_get_saturation_level(self):
    #     cat_1 = Cat(6)
    #     cat_1.run(4)
    #     cat_1.eat('fodder')
    #     self.assertEqual(cat_1.saturation_level, 55)


class TestWall(unittest.TestCase):

    wall_1 = Wall(5, 6)

    def test_wall_square(self):
        self.assertEqual(self.wall_1.wall_square(),
                         self.wall_1.height * self.wall_1.width)


if __name__ == '__main__':
    unittest.main()
