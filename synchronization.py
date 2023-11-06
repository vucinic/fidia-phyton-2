from threading import Lock, Thread, RLock

lock = RLock()


def t():
    lock.acquire()
    print('t1')
    t2()
    lock.release()


def t2():
    lock.acquire()
    print('t2')
    lock.release()


Thread(target=t).start()
