from threading import Lock, Thread


class ThPrinterParameters:
    def __init__(self, index: int = 0, lock: Lock = Lock()):
        self.__lock = lock
        self.__index = index
        self.s = "Nel mezzo del cammin di nostra vita" \
                 "mi ritrovai per una selva oscura," \
                 "ché la diritta via era smarrita."

    def get_lock(self):
        return self.__lock

    def get_index(self):
        return self.__index

    def set_index(self, i: int):
        self.__index = i


class ThPrinter(Thread):

    def __init__(self, parameters: ThPrinterParameters):
        super(ThPrinter, self).__init__()
        self.__parameters = parameters

    def run(self) -> None:
        is_finished = False
        while not is_finished:

            with self.__parameters.get_lock():

                i = self.__parameters.get_index()
                if i < 102:
                    # print(name, s[i]) #, end='')
                    print(self.__parameters.s[i], end='')
                    self.__parameters.set_index(i + 1)
                else:
                    is_finished = True



def main():
    pars = ThPrinterParameters()

    th1 = ThPrinter(pars)
    th2 = ThPrinter(pars)
    th3 = ThPrinter(pars)

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()


main()
