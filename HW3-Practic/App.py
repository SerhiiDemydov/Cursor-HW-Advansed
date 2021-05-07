from abc import ABC, abstractmethod
import random
import re


class Human(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, *args, **kwargs):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name: str, age: int, avail_money: (float, int), own_home: list = []):
        self.name = name
        self.age = age
        self.avail_money = float(avail_money)
        self.owm_home = own_home
        self.salary = random.randint(8000, 32000)

    def info(self):
        print(f'My name {self.name}. I am {self.age} years old.\n'
              f'Available money: {self.avail_money}\n'
              f'Having own home: {list(map(lambda x: x.area, self.owm_home))}\n'
              f'My salary: {self.salary}\n')

    def make_money(self):
        print(f'Available money before salary: {self.avail_money}')
        self.avail_money += self.salary
        print(f'Available money after salary: {self.avail_money}\n')

    def buy_house(self, realtor, house):
        if house not in realtor.avail_house:
            print(f'The realtor does not have this house\n')
        elif self.avail_money <= house.cost:
            print(f'{self.name} dont have money for buy this house\n')
        elif realtor.steal_money() <= 10:
            print(f'Realtor {realtor.name} steal money from {self.name}')
            self.avail_money -= house.cost
        else:
            print(f'{self.name} buy house in {house.area}\n')
            realtor.avail_house.remove(house)
            self.avail_money -= house.cost
            self.owm_home.append(house)


class House:
    def __init__(self, area: str, cost: (float, int)):
        self.area = area
        self.cost = float(cost)

    def apply_disc(self, disc):
        self.cost -= (self.cost * disc)


class RealtorInCity(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        instance = super().__call__(*args, **kwargs)
        if instance.__dict__['city'] not in cls._instances:
            cls._instances.update({instance.__dict__['city']: instance})
            # cls._instances.update({cls: args})
        else:
            for realtor in cls._instances:
                if realtor == instance.__dict__['city']:
                    raise Exception('In this city already have realtor')
        return cls._instances[instance.__dict__['city']]


class Realtor(metaclass=RealtorInCity):
    def __init__(self, name: str, city: str, avail_house: list = []):
        self.name = name
        self.city = city
        self._avail_house = self.__check_house(avail_house)
        self.discount = round(random.uniform(0, 0.3), 2)

    def __check_house(self, avail_house):
        list_houses = []
        for house in avail_house:
            if bool(re.search(self.city, house.area)):
                list_houses.append(house)
        return list_houses

    @property
    def avail_house(self):
        return self._avail_house

    @avail_house.setter
    def avail_house(self, avail_house):
        self._avail_house = self.__check_house(avail_house)

    def info_about_houses(self):
        print(f'Hello. My name {self.name}. I am realtor from {self.city}\n'
              f'\nList houses')
        for house in self.avail_house:
            print(f'\nInformation about house: {self.avail_house.index(house) + 1}\n'
                  f'Area: {house.area}\n'
                  f'Cost: {house.cost}\n')

    def give_discount(self, house):
        if house in self.avail_house:
            house.apply_disc(self.discount)
            print(f'Price after discount for house in {house.area}: {house.cost}')
        else:
            print(f'This house is not in the list of the realtor')

    def steal_money(self):
        return random.randrange(0, 100)


if __name__ == "__main__":
    house1 = House("Kyiv, Koshova 85", 30000)
    house2 = House("Kyiv, Akademika Vilyamsa 30", 45000)
    house3 = House("Lviv, Shevchenko 45", 34000)

    # Check all methods in class Realtor
    anna_realtor = Realtor("Anna", "Kyiv", [house1, house2, house3])
    print(f'\n\n-------------Anna realtor-------------\n')
    anna_realtor.info_about_houses()
    # Check setter
    anna_realtor.avail_house = [house3, house2, house1]
    anna_realtor.info_about_houses()
    anna_realtor.give_discount(house2)
    anna_realtor.give_discount(house3)

    jack_realtor = Realtor("Jack", "Lviv", [house1, house2, house3])
    print(f'\n\n-------------Jack realtor-------------\n')
    jack_realtor.info_about_houses()

    # Check all methods in class Person
    serhii_person = Person('Serhii', 25, 30000)
    print(f'\n\n-------------Serhii person-------------\n')
    serhii_person.info()
    serhii_person.buy_house(anna_realtor, house2)
    serhii_person.buy_house(anna_realtor, house3)
    serhii_person.make_money()
    serhii_person.info()
    serhii_person.buy_house(anna_realtor, house2)

    # Check parameters after the purchase
    print(f'\n\n-------------After the purchase-------------\n')
    anna_realtor.info_about_houses()
    serhii_person.info()

    # Check one realtor in one city
    steve_realtor = Realtor("Steve", "Kyiv", [house1, house2, house3])
