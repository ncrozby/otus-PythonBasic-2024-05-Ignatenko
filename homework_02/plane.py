"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle

class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0


    def load_cargo (self,add_cargo):
        new_cargo = self.cargo + add_cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload (f'overload plane{new_cargo}')
        else:
            self.cargo = new_cargo

    def remove_all_cargo (self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo