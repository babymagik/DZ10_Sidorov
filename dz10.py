from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()



class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus


pos = Position('Ivan', 'Ivanov', 'senior', {"wage": 15000.54, "bonus": 50000.8})
print(pos.get_full_name())
print(pos.get_total_income())

