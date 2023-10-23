import time
from threading import Thread

i = 0

s = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita."""


def func():
    global i
    while i < 102:
        print(s[i], end='')
        i += 1


def main():
    t1 = Thread(target=func)
    t2 = Thread(target=func)

    t1.start()
    t2.start()


def main():
    t1 = Thread(target=func)
    t2 = Thread(target=func)

    t1.start()
    t2.start()


c = 0


def _100_000_000():
    c = 0
    while c < 100_000_000:
        # print(c)
        c += 1


def alpha():
    c = "a"
    d = 0
    while d < 1000000:
        # print(c)
        c += "a"
        d += 1


t0 = time.time_ns()
_100_000_000()
alpha()
t1 = time.time_ns()

print(f'Elapsed {(t1 - t0) // 1_000_000}')

c = 0
t0 = time.time_ns()
t1 = Thread(target=_100_000_000)
t2 = Thread(target=alpha)
t1.start()
t2.start()
t1.join()
t2.join()
t1 = time.time_ns()

print(f'Elapsed {(t1 - t0) // 1_000_000}')
