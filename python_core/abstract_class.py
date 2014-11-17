"""
    Created on 06.10.2014

    @author: Oleksandr Poliatykin

    Интерфейсы, и абстрактные классы (роль простого интерфейса). Паттерн билдер
"""
import abc


class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        print("inside Car init")
        self.parts = []
        # pass

    @abc.abstractmethod
    def show(self):
        print("asss")
        # pass


class BMW(Car):
    def __init__(self):
        super().__init__()
        #self.parts = []
        #pass

    def show(self):
        for i in self.parts:
            i.show()

    def add_part(self, part):
        self.parts.append(part)


class CarPart(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def show(self):
        pass


class Motor(CarPart):
    def __init__(self, power):
        self.power = power

    def show(self):
        print("Power\t", self.power)


class Body(CarPart):
    def __init__(self, size):
        self.size = size

    def show(self):
        print("Size\t", self.size)


class Director:
    def __init__(self, builder):
        self.builder = builder

    def create_car(self):
        self.builder.build_motor()
        self.builder.build_body()


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.car = None

    @abc.abstractmethod
    def build_motor(self):
        pass

    @abc.abstractmethod
    def build_body(self):
        pass

    def get_car(self):
        return self.car


class BuilderBMW(Builder):
    def __init__(self):
        self.car = BMW()

    def build_body(self):
        body = Body(200)
        self.car.parts.append(body)

    def build_motor(self):
        m = Motor(100)
        self.car.parts.append(m)


def main():
    build = BuilderBMW()
    d = Director(build)
    d.create_car()
    car_c = build.get_car()
    car_c.show()
    # b = Car()


if __name__ == '__main__':
    main()