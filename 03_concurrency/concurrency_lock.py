from threading import Thread, Lock
from time import sleep

s = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita."""


def func(name, args):
    g_lock = args['g_lock']
    is_finished = False
    while not is_finished:
        g_lock.acquire()
        if args['current_index'] < 102:
            # print(name, s[i]) #, end='')
            print(s[args['current_index']], end='')
            args['current_index'] += 1
        else:
            is_finished = True

        sleep(100)
        g_lock.release()


def main():
    args = {
        'current_index': 0,
        'g_lock': Lock()
    }

    t1 = Thread(target=func, kwargs={"name": 't1', "args": args})
    t2 = Thread(target=func, kwargs={"name": 't2', "args": args})

    t1.start()
    t2.start()

    t1.join()
    t2.join()


main()
