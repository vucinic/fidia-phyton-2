class Point:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


def add_points(p1: Point, p2: Point) -> Point:
    return Point(p1.x + p2.x, p1.y + p2.y)
