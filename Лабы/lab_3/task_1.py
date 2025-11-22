class ShapeTest:
    def __init__(self, R):
        self.R = R

    def test_point(self, x, y):
        if (x == 0 and y == 0) or x ** 2 + y ** 2 == self.R ** 2 or (x - self.R) ** 2 + (y - self.R) ** 2 == self.R ** 2:
            return 'bound area'
        elif (y >= 0 and x >= 0) and x ** 2 + y ** 2 <= self.R ** 2:
            return 1
        elif (-self.R <= y <= 0 and -self.R <= x <= 0) and (x ** 2 + y ** 2 != self.R ** 2):
            return 2
        else:
            return 0


if __name__ == '__main__': # pragma: no cover
    R = int(input('Enter radius\n'))
    shape = ShapeTest(R)

    test_points = [
        (0, R),
        (-R, 0),
        (R/2, R/2),
        (-R/2, -R/4),
        (R * 3, 0)
    ]

    for point in test_points:
        result = shape.test_point(point[0], point[1])
        print(f"Point {point} is in this area: {result}")
