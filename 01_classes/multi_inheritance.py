class HasMother:

    def __init__(self, mothername):
        self.mothername = mothername

    def print(self):
        print('Mother: ' + self.mothername)


class HasFather:

    def __init__(self, fathername):
        self.fathername = fathername

    def print(self):
        print('Father: ' + self.fathername)


class Son(HasMother, HasFather):

    def __init__(self, mother, father):
        # super(HasMother, self).__init__(self, mother)
        # super(HasFather, self).__init__(self, father)
        HasMother.__init__(self, mother)
        HasFather.__init__(self, father)

    def __str__(self):
        super().print()
        # print("1 Father :", self.fathername)
        # print("1 Mother :", self.mothername)


p = Son('Lucia', 'Mario')
str_p = str(p)
print(p)
# p.print()

print(Son.mro())
