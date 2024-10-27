class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner} \n')

    def set_color(self, new_color):
        self.new_color = new_color
        lowercase_list = [s.lower() for s in Vehicle.__COLOR_VARIANTS]
        string_l = new_color.lower()
        if string_l in lowercase_list:
            self.__color = new_color
        else:
            print(f'"Нельзя сменить цвет для {self.__model} на {self.new_color}, т.к. его нет в каталоге.')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle2 = Sedan('Дед Афанасий', 'ВАЗ 2109', 'Вишнёвый', 72)

# Изначальные свойства
vehicle1.print_info()
vehicle2.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLaCK')
vehicle1.owner = 'Vasyok'

vehicle2.set_color('Мокрый асфальт')
vehicle2.set_color('BLaCK')
vehicle2.__model = 'Жигули'
vehicle2.owner = 'Внук Арсений'

# Проверяем что поменялось
vehicle1.print_info()
vehicle2.print_info()
