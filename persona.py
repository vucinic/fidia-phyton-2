
class Persona:
    __tot_persone = 0

    def __init__(self, nome, eta):
        Persona.__tot_persone += 1
        self.nome = nome
        self.eta = eta

    def __del__(self):
        Persona.__tot_persone -= 1

    def saluto(self):
        print(f"Ciao, il mio nome è {self.nome} e ho {self.eta} anni.")


print(Persona.__tot_persone)

p = Persona('Mario', 58)

print(Persona.__tot_persone)
print(p.__tot_persone)

print(p.nome)