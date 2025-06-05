# Задание 1
# Есть родительский класс:
# class Transport:
# def __init__(self, name, max_speed, mileage):
# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass

autobus = Autobus(name="Renaul Logan", max_speed=180, mileage=12)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")

# Задание 2
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного средства:
# class Transport:
# def __init__(self, name, max_speed, mileage):
# self.name = name
# self.max_speed = max_speed
# self.mileage = mileage
# def seating_capacity(self, capacity):
# return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

bus = Autobus("Renaul Logan", 120, 50000)
print(bus.seating_capacity())