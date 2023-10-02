class Vehicle:

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.__x: float = x
        self.__y: float = y
        self.__time: float = 0.0

    def get_position(self) -> tuple[float, float]:
        return self.__x, self.__y

    def move(self, new_x, new_y, vel):
        distance = ((new_x - self.__x) ** 2 + (new_y - self.__y) ** 2) ** 0.5
        self.__time += distance / vel
        self.__x = new_x
        self.__y = new_y

    def get_time(self) -> float:
        return self.__time


v = Vehicle()
print(v.get_position())
v.move(1, 1, 1)
print(v.get_position())
print(v.get_time())


v2 = Vehicle()
print(v2.get_position())
v2.move(10, 10, 50)
print(v2.get_position())
print(v2.get_time())

pos = v.get_position()
print(pos)
print(v.get_time())
