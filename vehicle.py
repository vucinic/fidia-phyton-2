class Vehicle:
    __vehicles_count = 0

    @classmethod
    def get_vehicles_count(cls):
        return cls.__vehicles_count

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.__x: float = x
        self.__y: float = y
        self._z: float = 0
        self.__time: float = 0.0
        Vehicle.__vehicles_count += 1

    def get_position(self) -> (float, float):
        return self.__x, self.__y

    def move(self, new_x, new_y, vel):
        distance = ((new_x - self.__x) ** 2 + (new_y - self.__y) ** 2) ** 0.5
        self.__time += distance / vel
        self.__x = new_x
        self.__y = new_y

    def get_time(self) -> float:
        return self.__time

    def get_X(self):
        return self.__x
    def get_Z(self):
        return self._z




