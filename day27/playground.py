
def add(*args):
    print(args[0])
    sum =0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 7, 2, 1, 9, 4))

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key,value)

    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self,**kw):
        #self.make= kw["make"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")

print(my_car.model)