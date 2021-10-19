# задание 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        mass = self._length * self._width * 25 * 0.05
        return mass


task_2 = Road(1000, 10)
print(int(task_2.mass_calc()), 'tons')


# задание 3

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


task_3 = Position('Nik', 'Kut', 'st', {'wage': 40000, 'bonus': 16000})
print(task_3.get_full_name())
print(task_3.get_total_income())


# задание 4

class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going'.format(self.name))

    def stop(self):
        print('{} is stopping'.format(self.name))

    def turn(self, direction):
        print('{} turn to the {}'.format(self.name, direction))

    def show_speed(self):
        print('Current speed: {}'.format(self.speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Your speed is more than max')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Work car current speed is ', self.speed)
        if self.speed > 40:
            print('Your speed is more than max')


class PoliceCar(Car):
    pass


sport_car = SportCar(300, 'Red', 'Porshe', False)
town_car = TownCar(100, 'Silver', 'Ford', False)
work_car = WorkCar(80, 'Black', 'Chevrolet', False)
police_car = PoliceCar(150, 'White-Blue', 'NYPD', True)

work_car.show_speed()
police_car.show_speed()
police_car.turn('left')
sport_car.go()
town_car.stop()


# задание 5

class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Обводка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Набросок карандашом')


class Handle(Stationery):
    def draw(self):
        print('Зарисовка маркером')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
print(pen.title)
pencil.draw()
handle.draw()


# задание 1

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__colour = (('Red', 7), ('Yellow', 2), ('Green', 3))

    def running(self):
        for colour, sec in cycle(self.__colour):
            print(colour, '(wait {} sec)'.format(sec))
            sleep(sec)


t_light = TrafficLight()
t_light.running()
