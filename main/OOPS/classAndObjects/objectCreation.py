class Laptop:
    def setval(self, name, model, year, ram, processor, price):
        self.name = name
        self.model = model
        self.year = year
        self.ram = ram
        self.processor = processor
        self.price = price

    def printval(self):
        print("Laptop name =", self.name)
        print("Model =", self.model)
        print("Year =", self.year)
        print("Ram =", self.ram)
        print("Processor =", self.processor)
        print("Price =", self.price)


a = Laptop()
a.setval("MacBook", "Air", "2017", "8", "Intel", "99999")
a.printval()

b = Laptop()
b.setval("AZUZ", "TUF", "2018", "8", "Intel", "69999")
b.printval()
