from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
#    weight = 2000
 #   fuel = 100
 #   fuel_consumption = 2
#    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False



    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError ('tank is empty')


    def move(self, distance):
        needed_fuel = self.fuel - (distance * self.fuel_consumption)
        if needed_fuel < 0:
            raise NotEnoughFuel(needed_fuel)
        else:
            self.fuel = needed_fuel





