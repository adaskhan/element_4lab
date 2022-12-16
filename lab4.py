from abc import abstractmethod, ABC


class Person:
    def __init__(self, full_name):
        self.full_name = full_name


class Driver(Person):
    def __init__(self, full_name, driving_experience):
        super().__init__(full_name)
        self.driving_experience = driving_experience


class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    @abstractmethod
    def start(self):
        print("Let's go!")

    @abstractmethod
    def stop(self):
        print("Stop!")

    @abstractmethod
    def turn_right(self):
        print("Turn right!")

    @abstractmethod
    def turn_left(self):
        print("Turn left!")

    def __str__(self):
        return f"Brand: {self.brand}, Class: {self.car_class}, Weight: {self.weight}, Driver: {self.driver.full_name}, Engine: {self.engine.manufacturer} ({self.engine.power} horsepower)"


class Lorry(Car, ABC):
    def __init__(self, brand, car_class, weight, driver, engine, load_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.load_capacity = load_capacity

    def __str__(self):
        return super().__str__() + f", Load Capacity: {self.load_capacity}"


class SportCar(Car, ABC):
    def __init__(self, brand, car_class, weight, driver, engine, speed_limit):
        super().__init__(brand, car_class, weight, driver, engine)
        self.speed_limit = speed_limit

    def __str__(self):
        return super().__str__() + f", Speed Limit: {self.speed_limit}"


if __name__ == '__main__':
    driver = Driver("Adaskhan Baglan", 5)
    engine = Engine(250, "Ford")
    car = Car("Ford", "Sedan", 1200, driver, engine)

    car.start()
    car.turn_left()
    car.stop()

    print(car)

    lorry = Lorry("Volvo", "Lorry", 5000, driver, engine, 10000)
    print(lorry)

    sport_car = SportCar("Porsche", "Sport", 1500, driver, engine, 280)
    print(sport_car)
