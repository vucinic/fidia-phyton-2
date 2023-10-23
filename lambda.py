from persona import Persona


def to_int(x):
    return int(x)


l = [0, 1, 2, 3, "0005", 4, 1, 0, 5, 6, 7, 8, 9]
print(sorted(l, key=to_int))

print(sorted(l, key=lambda x: int(x)))

p: list[Persona] = []
print(sorted(p, key=lambda x: x.nome))
