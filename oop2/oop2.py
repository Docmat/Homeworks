class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self,km):
        self.odometer += km
        print(f'odometer {self.odometer} km')


    def __subtract_fuel(self, km):
        fuel = km // 10
        if fuel <= self.fuel:
            self.__add_distance(km)
            self.fuel -= fuel
            print('Let’s drive!')
            print(f'Fuel {self.fuel} l')
        else:
            print('Need more fuel, please, fill more!')


    def drive(self,km):
        self.__subtract_fuel(km)

cr1 = Car("BMW","x5",2018)
cr1._Car__subtract_fuel(500)
cr1.drive(int(input("Введите км: ")))
