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

    t1.join()
    t2.join()
