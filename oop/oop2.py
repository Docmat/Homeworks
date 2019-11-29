class Airplane:
    def __init__(self,make,model,year,max_speed):

        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True

    def land(self):
        self.is_flying = False

    def fly(self,km):
        self.odometer +=km


airbus = Airplane("Boing","727","2007","1200km/h")

airbus.take_off()
print(airbus.model)

print(airbus.is_flying)
