from abc import ABC, abstractmethod


class Processable(ABC):

    @abstractmethod
    def _extract(self):
        pass

    @abstractmethod
    def _transform(self):
        pass

    @abstractmethod
    def _adapt(self):
        pass

    @abstractmethod
    def _save(self):
        pass

    def process(self):
        self._extract()
        self._transform()
        self._adapt()
        self._save()


class TxtProcessor(Processable):

    def __init__(self, in_path: str):
        self.__filename = in_path
        self.__file = None

    def _extract(self):
        self.__file = open(self.__filename)

    def _transform(self):
        pass

    def _adapt(self):
        pass

    def _save(self):
        pass


class CsvProcessor(Processable):

    def __init__(self, in_path: str):
        self.__filename = in_path
        self.__file = None

    def _extract(self):
        self.__file = open(self.__filename)

    def _transform(self):
        pass

    def _adapt(self):
        pass

    def _save(self):
        pass


def process_all(all: list[Processable]):
    for i in all:
        i.process()


t_proc = TxtProcessor('in.txt')
c_proc = CsvProcessor('in.csv')

process_all([t_proc, c_proc])
