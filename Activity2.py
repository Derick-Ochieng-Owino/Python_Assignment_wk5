class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying")

class Ship(Vehicle):
    def move(self):
        print(f"{self.name} is sailing")

class Train(Vehicle):
    def move(self):
        print(f"{self.name} is chugging")

class Hovercraft(Vehicle):
    def move(self):
        print(f"{self.name} is hovering")

vehicles = [
    Car("Mercedes"),
    Plane("Blackbird"),
    Ship("Titanic"),
    Train("SGR"),
    Hovercraft("SR.N4")
]

for vehicle in vehicles:
    vehicle.move()