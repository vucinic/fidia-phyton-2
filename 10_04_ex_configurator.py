from abc import ABC, abstractmethod


class Part(ABC):

    @abstractmethod
    def get_part_number(self):
        pass

    @abstractmethod
    def get_serial_number(self):
        pass


class Tavola(Part):
    # todo

    pass


class ElettroMandrino(Part):
    pass


class Machine(ABC):

    @abstractmethod
    def add_part(self, p: Part):
        pass

    def print(self):
        # todo
        pass


class Gtf(Machine):
    pass


class K211(Machine):
    pass


def add_part_to_all(p: Part, machines: list[Machine]):
    for m in machines:
        m.add_part(p)


m: Machine = K211()
m1: Machine = Gtf()

add_part_to_all(Tavola(), [m, m1])
