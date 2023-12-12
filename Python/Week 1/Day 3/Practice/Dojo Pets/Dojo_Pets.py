from Ninja_Class import Ninja
from Pet_Class import Pet


pet=Pet("Gato","cat","scratch")
ninja=Ninja("Mao","Tzu", pet,"Ball", "Ham" )
ninja.walk().feed().bathe()


class Cat(Pet):
    def __init__(self,age, health=10, energy=10, name="", type="", tricks="",):
        super().__init__(health, energy, name, type, tricks)
        self.age=age
    

