class Data:

    def __init__(self,
                 g: int = None,
                 m: int = None,
                 a: int = None):
        self.__g = g if g is not None else 0
        self.__m = m if m is not None else 0
        self.__a = a if a is not None else 0

    def set_m(self, m):
        self.__m = m

    def get_m(self):
        return self.__m

    def diff(self, other):
        """
        :param other: controlla che sia di tipo Data e se tipo data fa differenza in giorni self - other
        :return: differenza in giorni
        """
        if not isinstance(other, Data):
            raise Exception('other tdeve essere una Data')

        a_diff = self.__a - other.__a
        return a_diff

    def epoch_time(self):
        """
        :return: numero di secondi dal 1/1/1970
        """
        pass

    def __del__(self):
        print("Elimino oggetto " +
              str(self.__g) + ' ' +
              str(self.__m) + ' ' +
              str(self.__a)
              )


a = Data(1, 1, 2023)
b = Data(1, 1, 1000)

print(a.diff(b))
print(b.diff(a))


# print(a.diff(b))
