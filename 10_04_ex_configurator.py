from abc import ABC, abstractmethod


class Part(ABC):

    @abstractmethod
    def get_part_number(self) -> str:
        pass

    @abstractmethod
    def get_serial_number(self) -> str:
        pass


class Tavola(Part):
    def get_part_number(self):
        return self.__part

    def get_serial_number(self):
        return self.__serial

    def __init__(self, id: str):
        if len(id.split('#')) != 2:
            raise Exception('Wrong id format')
        self.__part = id.split('#')[1]
        self.__serial = id.split('#')[0]


class ElettroMandrino(Part):
    def get_part_number(self):
        return self.__part

    def get_serial_number(self):
        return self.__serial

    def __init__(self, serial: str, part: str):
        self.__part = part
        self.__serial = serial


class Machine(ABC):

    def __init__(self):
        self._parts = list()

    @abstractmethod
    def add_part(self, p: Part):
        pass

    def print(self):
        print('-----------')
        for p in self._parts:
            print(p.get_serial_number(), end=' ')
            print(p.get_part_number())
        print('-----------')


class GtfPartError(Exception):
    pass


class Gtf(Machine):

    def add_part(self, p: Part):
        if not p.get_serial_number().startswith("900"):
            raise GtfPartError("Parts serial must start with 900")
        self._parts.append(p)


class K211(Machine):

    def add_part(self, p: Part):
        self._parts.append(p)


def add_part_to_all(p: Part, machines: list[Machine]):
    for machine in machines:
        machine.add_part(p)


m: Machine = K211()
m1: Machine = Gtf()

add_part_to_all(Tavola("900011211#p343"), [m, m1])
add_part_to_all(ElettroMandrino("s9001211", "p343"), [m, m1])

print("m")
m.print()

print("m1")
m1.print()

