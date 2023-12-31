
class Persona:
    __tot_persone = 0

    @classmethod
    def set_tot_persone(cls, tot: int):
        cls.__tot_persone = tot

    def __init__(self, nome, eta):
        Persona.__tot_persone += 1
        self.nome = nome
        self.eta = eta

    def __del__(self):
        Persona.__tot_persone -= 1

    def saluto(self):
        print(f"Ciao, il mio nome è {self.nome} e ho {self.eta} anni.")


p = Persona('Mario', 58)


p.saluto()
print(p.nome)


Persona.set_tot_persone(1000)
