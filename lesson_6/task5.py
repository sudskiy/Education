#  Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
#  (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
#  Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
#  выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
#  экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super().__init__('Pen')

    def draw(self):
        print("Ручкой пишешь ты")


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Pencil')

    def draw(self):
        print("Карандаш используем")


class Handle(Stationery):
    def __init__(self):
        super().__init__('Handle')

    def draw(self):
        print("Маркер в руку лег")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
