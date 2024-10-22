class Car():
    '''Простая модель автомобиля'''


    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year



    def get_descriptive_name(self):
        '''Возвращает аккуратно отформатированное описание'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()