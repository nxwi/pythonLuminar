# Create a class car with attribute company_name, model, fuel_type, color, transmission, price
# for setting the value create setvalue()
# for displaying the object create display()
# create three objects

class Car:
    def setvalue(self, company_name, model, fuel_type, color, transmission, price):
        self.company_name = company_name
        self.model = model
        self.fuel_type = fuel_type
        self.color = color
        self.transmission = transmission
        self.price = price

    def display(self):
        print("Company name =", self.company_name)
        print("Model =", self.model)
        print("Fuel type =", self.fuel_type)
        print("Color =", self.color)
        print("Transmission =", self.transmission)
        print("Price =", self.price)
        print("====================")


a = Car()
a.setvalue("Toyota", "Camry", "Gasoline", "Silver", "Automatic", "$26,000")
a.display()

b = Car()
b.setvalue("Honda", "Civic", "Gasoline", "Black", "Manual", "$22,000")
b.display()

c = Car()
c.setvalue("Hyundai", "Elantra", "Gasoline", "Blue", "Automatic", "$20,000")
c.display()
