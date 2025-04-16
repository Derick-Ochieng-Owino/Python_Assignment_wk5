class Superhero:
    def __init__(self, name, power, age, airborne, strength):
        self.name = name
        self._power = power
        self._age = age
        self.airborne = airborne
        self.strength = strength
        self.energy = 100
    
    def use_power(self):
        if self.energy >= 20:
            print(f"{self.name} uses {self._power}!")
            self.energy -= 20
        else:
            print(f"{self.name} is too tired to use powers!")
    
    def train(self):
        self.strength += 5
        print(f"{self.name} trains and gains strength! New strength: {self.strength}")
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, new_power):
        if len(new_power) > 0:
            self._power = new_power
        else:
            print("Power cannot be empty!")
    
    def __str__(self):
        return f"{self.name} ({'Airborne' if self.airborne else 'Ground-based'}): Power - {self._power}, Strength - {self.strength}"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, age, strength, max_altitude):
        super().__init__(name, power, age, True, strength)
        self.max_altitude = max_altitude
    
    def fly(self):
        print(f"{self.name} soars through the air at max altitude of {self.max_altitude} feet!")


if __name__ == "__main__":
    superhero1 = Superhero("Superman", "Laser Eyes", 30, True, 100)
    superhero2 = Superhero("Batman", "Intelligence", 35, False, 80)
    superhero3 = FlyingSuperhero("Omni Man", "Flight", 40, 90, 50000)
    superhero4 = Superhero("Spiderman", "Web-Slinging", 25, True, 70)
    superhero5 = FlyingSuperhero("Invincible", "Super Strength", 20, 85, 60000)
    superhero6 = Superhero("Green Lantern", "Energy Constructs", 28, True, 95)
    
    print(superhero2.name)
    superhero1.use_power()
    superhero3.fly()
    
    print("\nSuperhero info:")
    print(superhero1)
    print(superhero3)