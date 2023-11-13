import time
from random import randint
from threading import Condition, Thread

numbers = []
c = Condition()

kill = False


def producer():
    while not kill:
        with c:
            num = randint(1, 10)
            print("Generato:", num)
            numbers.append(num)
            print("Notifico")
            c.notify()

def consumer():
    while not kill:
        with c:
            print("\tAspetto")
            c.wait()
            print("\tPreso", numbers.pop())


cons = Thread(target=consumer)
prod = Thread(target=producer)

cons.start()

time.sleep(2)

prod.start()

time.sleep(10)
kill = True

prod.join()
cons.join()
