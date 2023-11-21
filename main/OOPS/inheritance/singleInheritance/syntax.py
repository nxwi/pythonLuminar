class parent:
    def parentfun(self):
        print("This is parent class")


class Child(parent):
    def childfun(self):
        print("This is child class")


obj = Child()
obj.parentfun()
obj.childfun()
