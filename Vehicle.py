class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start(self):
        print(f"{self.brand} {self.model} is starting ")

class Car(Vehicle):
    def play_music(self):
        print("Playing music in the car.")

class ElectricCar(Car):
    def charge(self):
        print("Charging the electric car.")

class SmartDevice:
    def connect_wifi(self):
        print("Connecting to Wi-Fi.")

class SmartCar(Car, SmartDevice):
    def auto_drive(self):
        print("Smart car is driving automatically.")

class Bike(Vehicle):
    def kick_start(self):
        print("Bike is kick-started.")

class ElectricSmartCar(SmartCar, ElectricCar):
    def autopilot_mode(self):
        print("Autopilot mode activated.")

esc = ElectricSmartCar("Tesla", "Model S")
esc.start()
esc.play_music()
esc.connect_wifi()
esc.charge() 
esc.autopilot_mode()