"""3.
class Profile:
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
"""
import inspect


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.descriptions = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]
        print(f'{self.name} successful create')

    def __call__(self, *args, **kwargs):
        print(f'It is object {self.name}')

    def __str__(self):
        return f'{self.descriptions}'


Person1 = Profile('Serhii', 'Demydov', '+39046587231', 'Kyiv', 'serj@gmail.com', '24.05.1995', '25', 'male')
Person1()
print(Person1)