from threading import Thread, RLock

lock = RLock()


def t():
    with lock:
        print('t1')
        t2()


def t2():
    with lock:
        print('t2')


Thread(target=t).start()
