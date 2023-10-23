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


class SerialBus(ABC):

    @abstractmethod
    def open_communication(self):
        pass

    @abstractmethod
    def write_bytes(self, buffer: bytes):
        pass

    @abstractmethod
    def read_bytes(self) -> bytes:
        pass

    @abstractmethod
    def close_communication(self):
        pass


class Machine(ABC):

    @abstractmethod
    def get_serial_bus(self) -> SerialBus:
        pass

    @abstractmethod
    def add_part(self, p: Part):
        pass

    @abstractmethod
    def print(self):
        pass
        # print('-----------')
        # for p in self._parts:
        #     print(p.get_serial_number(), end=' ')
        #     print(p.get_part_number())
        # print('-----------')


class GtfPartError(Exception):
    pass


class Gtf(Machine):

    def get_serial_bus(self) -> SerialBus:
        return self.__serial_bus

    def __init__(self):
        self.__parts_left = list()
        self.__parts_right = list()

    def print(self):
        pass

    def add_part(self, p: Part):
        if not p.get_serial_number().startswith("900"):
            raise GtfPartError("Parts serial must start with 900")
        self._parts.append(p)


class K211(Machine):

    def add_part(self, p: Part):
        self._parts.append(p)


def add_part_to_all(p: Part, machines: list[Machine]):
    for machine in machines:
        try:
            machine.add_part(p)
        except GtfPartError as e:
            print('Error while adding part:', e)
        except Exception:
            print("Generic Error")


m_k211: Machine = K211()
m_gtf: Machine = Gtf()
mm = Machine()

m_gtf.get_serial_bus().open_communication()
m_gtf.get_serial_bus().write_bytes(bytes('ciao'))

add_part_to_all(Tavola("900011211#p343"), [m_k211, m_gtf])
add_part_to_all(ElettroMandrino("s9001211", "p343"), [m_k211, m_gtf])

print("m")
m_k211.print()

print("m1")
m_gtf.print()
