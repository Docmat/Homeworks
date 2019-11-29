class Car:
    def __init__(self,owner,make,model,year):
        self.owner = owner
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.is_going = False


    def go(self, km):
        self.is_going = True
        self.odometer += km

    def stop(self):
        self.is_going = False


car = Car("Doc","Toyota","Camry","2015")

car.go(500)
print(car.odometer, "\n", car.is_going)

print(car.model)
car.stop()
print(car.is_going)
