class Car():
    '''Простая модель автомобиля'''


    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        '''Возвращает аккуратно отформатированное описание'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        '''Вывод пробег машины в милях'''
        print(f"This car has {self.odometer_reading} miles on it")


    def update_odometer(self, milieage):
        '''Устанавливает заданное значение на одометре
        При попытке обратной открутке изменения отклоняются'''
        if milieage >= self.odometer_reading:
            self.odometer_reading = milieage
        else:
            print("Одометр скручивать нельзя")