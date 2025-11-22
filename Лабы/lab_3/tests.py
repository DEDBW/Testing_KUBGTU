import unittest
from task_1 import ShapeTest


class TestShapeTest(unittest.TestCase):

    def setUp(self):
        self.R = 5
        self.shape = ShapeTest(self.R)

    def test_on_boundary(self):
        self.assertEqual(self.shape.test_point(0, 0), 'bound area')
        self.assertEqual(self.shape.test_point(self.R, 0), 'bound area')
        self.assertEqual(self.shape.test_point(0, self.R), 'bound area')

    def test_outside_circle(self):
        self.assertEqual(self.shape.test_point(self.R * 3, 0), 0)
        self.assertEqual(self.shape.test_point(0, self.R * 2), 0)

    def test_inside_area_1(self):
        self.assertEqual(self.shape.test_point(2, 2), 1)
        self.assertEqual(self.shape.test_point(self.R / 2, self.R / 2), 1)

    def test_inside_area_2(self):
        self.assertEqual(self.shape.test_point(-2, -2), 2)
        self.assertEqual(self.shape.test_point(-self.R / 2, -self.R / 4), 2)

    def test_invalid_values(self):
        shape_with_zero_radius = ShapeTest(0)
        self.assertEqual(shape_with_zero_radius.test_point(0, 0), 'bound area')
        self.assertEqual(shape_with_zero_radius.test_point(1, 1), 0)

    def test_negative_radius(self):
        shape_negative = ShapeTest(-5)
        result = shape_negative.test_point(0, 0)
        self.assertIsNotNone(result)

    def test_string_coordinates(self):
        with self.assertRaises(TypeError):
            self.shape.test_point("строка", 5)
        with self.assertRaises(TypeError):
            self.shape.test_point(5, "строка")

    def test_none_radius(self):
        with self.assertRaises(TypeError):
            shape_invalid = ShapeTest(None)
            shape_invalid.test_point(1, 1)


if __name__ == '__main__':
    unittest.main()
