import threading
from threading import Thread
from time import sleep


class BlockingQueue:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.__open = True
        self.__buffer = list()
        self.__not_empty_condition = threading.Condition()
        self.__not_full_condition = threading.Condition()

    def get(self):
        """
        blocca se non ci sono elementi
        se la coda è chiusa ritorna None
        :return:
        """
        if not self.__open:
            return None

        with self.__not_empty_condition:
            while len(self.__buffer) == 0 and self.__open:
                self.__not_empty_condition.wait()

        if not self.__open:
            return None

        with self.__not_full_condition:
            ret = self.__buffer.pop(0)
            self.__not_full_condition.notify()

        return ret

    def put(self, el: object):
        """
        blocca se qualcuno sta leggendo un elemento,
        blocca se la coda è piena,
        inserisce l'elemento nella coda

        se la coda è chiusa ritorna False altrimenti True
        :param el:
        :return:
        """
        if not self.__open:
            return False

        with self.__not_full_condition:
            while len(self.__buffer) == self.max_size and self.__open:
                self.__not_full_condition.wait()

        if not self.__open:
            return False

        with self.__not_empty_condition:
            self.__buffer.append(el)
            self.__not_empty_condition.notify()

        return True

    def is_open(self):
        return self.__open

    def close(self):
        with self.__not_full_condition:
            with self.__not_empty_condition:
                self.__open = False
                self.__not_full_condition.notify_all()
                self.__not_empty_condition.notify_all()

    def __str__(self):
        return str(self.__buffer)


def insert(q: BlockingQueue, n: int, prefix: str):
    for i in range(n):
        print(prefix, 'insert', 1)
        if not q.put(1):
            return


def extract(q: BlockingQueue, prefix: str):
    i = 0
    while q.is_open():
        v = q.get()
        if v is None:
            print(prefix, 'coda chiusa, termino')
            break
        print(prefix, v)
        i += v
    print(prefix, ' total', i)


def real_main():
    q = BlockingQueue(10)

    ti1 = Thread(target=insert, args=(q, 1000, '1)'))
    ti2 = Thread(target=insert, args=(q, 3000, '2)'))
    ti3 = Thread(target=insert, args=(q, 2000, '3)'))

    te1 = Thread(target=extract, args=(q, 'ext)'))

    te1.start()
    ti1.start()
    ti2.start()
    ti3.start()

    sleep(3)
    q.close()

    te1.join()
    ti1.join()
    ti2.join()
    ti3.join()


def test_main():
    q = BlockingQueue(10)
    q.put(1)
    q.put("2")
    q.put(3)
    q.put("4")
    q.put(5)
    q.put("6")
    q.put(7)
    q.put("8")
    q.put(9)
    q.put("10")
    q.put("Ciccio")
    q.put("Ciccio")
    q.put("Ciccio")

    print(q)

    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())

    print(q)

    q.close()
    print(q.get())


real_main()
