"""
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
"""
from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPlaptop(Laptop):
    def __init__(self, model, screen_size, keyboard_type, touchpad_type, webcam_type, port_quantity, dynamics_type):
        self.model = model
        self.screen_size = screen_size
        self.keyboard_type = keyboard_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.port_quantity = port_quantity
        self.dynamics_type = dynamics_type
        print(f'{self.model} successful create')

    def screen(self):
        print(f'Screen: {self.screen_size}')

    def keyboard(self):
        print(f'Keyboard language: {self.keyboard_type}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_type}')

    def webcam(self):
        print(f'Webcam: {self.webcam_type}')

    def ports(self):
        print(f'Ports: {self.port_quantity}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_type}')


laptop1 = HPlaptop('HP Laptop 15s-eq1026ur', '15.6" SVA (1920x1080) Full HD', 'RU-EN', 'YES', 'HD 720p 1280x720',
                   '2 x USB 3.1 Gen 1 (Type-A) / 1 x USB 3.1 Gen 1 (Type-C) / HDMI ', '2.0 OEM ')

laptop1.screen()
laptop1.keyboard()
laptop1.touchpad()
laptop1.webcam()
laptop1.ports()
laptop1.dynamics()
