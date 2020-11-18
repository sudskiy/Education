# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 50
    color = "Black"
    name = "Lada"
    is_police = False

    def go(self):
        print("Тронулись!")

    def stop(self):
        print("Остановились")

    def turn(self, direction):
        self.direction = direction
        if direction.lower().__contains__("право"):
            print("Ёхаем направо")
        elif direction.lower().__contains__("лево"):
            print("Ёхаем налево")
        else:
            print("А у вас руль отвалился...")


    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("И куда мы так летим?")


class SportCar(Car):

    def go(self):
        print("Уходим в точку")


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("На тот свет спешим?")


class PoliceCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Стоять бояться!")


print(Car.speed)
a = TownCar()
b = SportCar()
c = WorkCar()
a.turn("Направо")
b.stop()
c.show_speed()
