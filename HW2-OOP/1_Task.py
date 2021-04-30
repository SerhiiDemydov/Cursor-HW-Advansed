"""

1.Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class

class Animals:
    Parent class, should have eat, sleep

class Animal1(Animal):
    Some of the animal with 1-2 extra methods related to this animal
"""


class Animal:
    def eat(self):
        print(f'{self.__class__.__name__} eating')

    def sleep(self):
        print(f'{self.__class__.__name__} sleeping')


class Fish(Animal):
    def swim(self):
        print(f'{__class__.__name__} swimming')


class Bird(Animal):
    def fly(self):
        print(f'{__class__.__name__} flying')


class Snake(Animal):
    def crawl(self):
        print(f'{__class__.__name__} crawling')


class Frog(Animal):
    def jump(self):
        print(f'{__class__.__name__} jumping')


class Horse(Animal):
    def run(self):
        print(f'{__class__.__name__} running')


fish = Fish()
bird = Bird()
snake = Snake()
frog = Frog()
horse = Horse()

print('-------------------------Taks 1-------------------------')
bird.eat()
snake.sleep()

print(f'Object fish is an instance of the Animals class: {isinstance(fish, Animal)}')
print(f'Object bird is an instance of the Animals class: {isinstance(fish, Animal)}')
print(f'Object snake is an instance of the Animals class: {isinstance(fish, Animal)}')
print(f'Object frog is an instance of the Animals class: {isinstance(fish, Animal)}')
print(f'Object horse is an instance of the Animals class: {isinstance(fish, Animal)}')

"""
1.a.Create a new class Human and use multiple inheritance to create Centaur class,
create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    Human class, should have eat, sleep, study, work

class Centaur(.., ..):
    Centaur class should be inherited from Human and Animal and has unique method related to it.
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'Human with name {self.name} eating')

    def sleep(self):
        print(f'Human with name {self.age} eating')

    def work(self):
        if self.age < 21:
            print(f'{self.name} so young for work')
        else:
            print(f'{self.name} working')

    def study(self):
        print(f'{self.name} studying')


class Centaur(Animal, Human):
    def run(self):
        print(f'Centaur {self.name} running')

    def human_eat(self):
        Human.eat(self)


centaur = Centaur('Jack', 25)
print('\n\n-------------------------Taks 1.a-------------------------')
centaur.eat()
centaur.human_eat()
centaur.sleep()
centaur.work()
centaur.run()
