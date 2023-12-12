class Ninja():
    def __init__(self,first,last,pet,treats,food):
        self.first_name=first
        self.last_name=last
        self.pet=pet
        self.treats=treats
        self.pet_food=food

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self