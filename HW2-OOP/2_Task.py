"""
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
  a.

class Person:
    Make the class with composition.

class Arm:
    Make the class with composition.
"""


class Person:
    def __init__(self):
        arm_left = Arm("Left arm")
        arm_right = Arm("Right arm")
        self.arms = [arm_left, arm_right]


class Arm:
    def __init__(self, descriptions):
        self.descriptions = descriptions


person1 = Person()
for arm in person1.arms:
    print(arm.descriptions)

"""
b.

class CellPhone:
    Make the class with aggregation

class Screen:
    Make the class with aggregation
"""


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, size="16:9"):
        self.size = size


screen1 = Screen()
phone1 = CellPhone(screen1)
print(phone1.screen.size)
