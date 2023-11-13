from threading import Thread


def routine(name='default'):
    # nome = ciccio['nome']
    i = 0
    while i < 10_000_000:
        if i % 10000 == 0:
            print(f'{name} {i}')
        i += 1


t = Thread(target=routine, kwargs={"name": "t1"})
t2 = Thread(target=routine, kwargs={"name": "t2"})
t.start()
t2.start()

print('Thread principale finito')

print('Aspetto thread secondari')

t.join()
t2.join()

print('Tutto finito')

