class Encapsulation:
    def examples(self, name, salary, address):
        self.name = name  # public data member
        self.__salary = salary  # private data member
        self._address = address  # protected data member

    def display0(self):  # public
        pass

    def __display1(self):  # private
        pass

    def _display2(self):  # protected
        pass
