class Car:

    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        print(kw)

new_car = Car(make = "nissan" , model = "GT-R")
print(new_car.model)