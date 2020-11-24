# 4.Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5.Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6.Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

class FreePlacesError(Exception):
    def __init__(self, txt=''):
        self.txt = txt


class HasEquipmentError(Exception):
    def __init__(self, txt=''):
        self.txt = txt


class Storage:
    __storages = []

    def __init__(self, name, places):
        self.__name = name
        self.__places = places
        self.equipment = []
        if self.__name not in self.__storages:
            self.__storages.append(self.__name)

    @classmethod
    def get_storages(cls):
        return cls.__storages

    @property
    def get_equipment(self):
        return self.equipment

    @property
    def get_places(self):
        return self.__places

    @staticmethod
    def get_idx(el_list, model, brand):
        length = len(el_list)
        for idx in range(length):
            if model in el_list[idx].values() and brand in el_list[idx].values():
                return idx
        return -1

    def add_equipment(self, **kwargs):
        eq = kwargs
        length = len(self.equipment)

        if self.get_places - eq['amount'] >= 0:
            if length > 0:
                idx = Storage.get_idx(self.equipment, eq['model'], eq['brand'])
                if not idx < 0:
                    self.equipment[idx]['amount'] += eq['amount']
                else:
                    self.equipment.append(eq)
            else:
                self.equipment.append(eq)
            self.__places -= eq['amount']
        else:
            raise FreePlacesError('На складе недостаточно места!')

    def send_equipment(self, brand, model, amount):
        idx = Storage.get_idx(self.equipment, model, brand)
        if not idx < 0:
            if amount < self.equipment[idx]['amount']:
                self.equipment[idx]['amount'] -= amount
            elif amount == self.equipment[idx]['amount']:
                del(self.equipment[idx])
            else:
                raise HasEquipmentError('На складе недостаточно такого товара!')
        else:
            raise HasEquipmentError('Такого товара нет на складе!')


class Equipment:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return f'EQ: {self.kwargs}'

    def send_to_storage(self, storage):
        storage.add_equipment(**self.kwargs)


class Printer(Equipment):
    def __init__(self, method='laser', colored=False, **kwargs):
        super().__init__(**kwargs)
        self.method = method
        self.colored = colored
        self.__obj = {**kwargs}
        self.__obj.update(method=self.method, colored=self.colored)

    def __str__(self):
        return f'PR: {self.__obj}'

    def send_to_storage(self, storage):
        storage.add_equipment(**self.__obj)

    def print_page(self):
        print('Печатаю пробную страницу')


class Scanner(Equipment):
    def __init__(self, resolution='1200', **kwargs):
        super().__init__(**kwargs)
        self.resolution = resolution
        self.__obj = {**kwargs}
        self.__obj.update(resolution=self.resolution)

    def __str__(self):
        return f'SC: {self.__obj}'

    def send_to_storage(self, storage):
        storage.add_equipment(**self.__obj)

    def scan_page(self):
        print('Страница отсканированна')


class Copier(Equipment):
    def __init__(self, colored=False, **kwargs):
        super().__init__(**kwargs)
        self.colored = colored
        self.__obj = {**kwargs}
        self.__obj.update(colored=self.colored)

    def __str__(self):
        return f'PR: {self.__obj}'

    def send_to_storage(self, storage):
        storage.add_equipment(**self.__obj)

    def copy_page(self):
        print('Копия страницы готова')


if __name__ == '__main__':
    main_storage = Storage('Центральны склад', 10)
    small_storage = Storage('Малый склад', 5)

    print('Storages:', Storage.get_storages())
    print('*' * 30 + '\n')

    eq_1 = Equipment(brand='HP', model='LaserJet-1010', price=150, amount=2)
    eq_1.send_to_storage(main_storage)
    print(eq_1)

    printer_1 = Printer(brand='HP', model='LaserJet-1010', price=150, amount=2)
    printer_2 = Printer(brand='HP', model='InkJet-1010', price=100, amount=3, colored=True, method='Ink')
    printer_1.send_to_storage(small_storage)
    printer_2.send_to_storage(small_storage)
    print(printer_1)
    print(printer_2)

    sc_1 = Scanner(brand='HP', model='ScanJet-1010', price=120, amount=2)
    sc_2 = Scanner(brand='HP', model='ScanJet-2020', price=120, amount=2, resolution='2400')
    try:
        sc_1.send_to_storage(small_storage)
    except FreePlacesError as e:
        print(e)

    try:
        main_storage.send_equipment(brand='Xerox', model='Ink-5', amount=1)
    except HasEquipmentError as e:
        print(e)
    try:
        small_storage.send_equipment(brand='HP', model='InkJet-1010', amount=5)
    except HasEquipmentError as e:
        print(e)

    print('\n' + '*' * 30)
    print('Small:', small_storage.get_equipment)
    print('Main', main_storage.get_equipment)
