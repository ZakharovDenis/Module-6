class Vehicle:
    __COLOR_VARIANTS = ['green', 'yellow', 'red', 'white', 'black', 'magenta']
    def __init__(self, owner:str, __model:str, __color , __engine_power):
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.owner = owner



    def get_model(self):
        print ('Модель:', self.__model)
    def get_horsepower(self):
        print('Мощность двигателя:', self.__engine_power)
    def get_color(self):
        print(f'Цвет:'), self.__color

    def print_info(self):
        print('Модель:', self.__model)
        print('Мощность двигателя:', self.__engine_power)
        print('Цвет:', self.__color)
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            print('Нельзя сменить цвет на Pink')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()