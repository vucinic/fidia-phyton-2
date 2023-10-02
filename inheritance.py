class Person(object):

    def __init__(self, name: str, lastname, height=0.0, size='M'):
        self.__name = name
        self.__lastname = lastname
        self.__height = height

    def display(self):
        print(self.__name)
        print(self.__lastname)


class Employee(Person):

    def __init__(self, fullname: str, salary: float, children):
        super().__init__(fullname.split(" ")[0], fullname.split(" ")[1])
        # Person.__init__(self, name, idnumber)
        self.__salary = salary


person = Employee("mario rossi", 25000)
Person()
print()
