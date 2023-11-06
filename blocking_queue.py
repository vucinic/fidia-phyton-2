from threading import Thread
from time import sleep


class BlockingQueue:

    def __init__(self, size: int):
        self.size = size
        self.__open = True

    def get(self):
        """
        blocca se non ci sono elementi
        :return:
        """
        pass

    def put(self, el: object):
        """
        blocca se qualcuno sta leggendo un elemento,
        blocca se la coda è piena,
        inserisce l'elemento nella coda
        :param el:
        :return:
        """
        pass

    def is_open(self):
        pass

    def close(self):
        pass


def insert(q: BlockingQueue, n: int):
    for i in range(n):
        q.put(i)


def extract(q: BlockingQueue):
    while q.is_open():
        print(q.get())


q = BlockingQueue(10)

ti1 = Thread(target=insert, args=(q, 1000))
ti2 = Thread(target=insert, args=(q, 3000))
ti3 = Thread(target=insert, args=(q, 2000))

te1 = Thread(target=extract, args=(q,))

te1.start()
ti1.start()
ti2.start()
ti3.start()

sleep(10)
q.close()

te1.join()
ti1.join()
ti2.join()
ti3.join()
