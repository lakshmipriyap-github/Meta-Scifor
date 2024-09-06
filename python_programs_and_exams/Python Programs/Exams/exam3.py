'''
In a magical kingdom, creatures have unique powers. Dragons breathe
fire, while Phoenixes rise from ashes. Create a class Creature with
power() method. Derive Dragon and Phoenix classes inheriting Creature.
Implement recursion to display the power of each creature. Instructions:
Define a Creature class with a power() method that returns the
creature's power. Create Dragon and Phoenix classes inheriting
Creature, overriding the power() method. Use recursion to display the
powers of both a Dragon
and a Phoenix.
'''
class Creature:
    def __init__(self):
        self.pow = "Creature's Power"

    def power(self):
        return self.pow

class Dragon(Creature):
    def __init__(self):
        self.pow = "Dragon Breathe's fire"
    def power(self):
        # p1 = super().power()
        return self.pow

class Phoenix(Creature):
    def __init__(self):
        self.pow = "Phoenix's rise from ash"

    def power(self):
        # p2 = super().power()
        return self.pow

def ShowPower(obj):
    print(f"{obj.power()}")

objCreature = Creature()
objDragon = Dragon()
objPhoenix = Phoenix()

ShowPower(objCreature)
ShowPower(objDragon)
ShowPower(objPhoenix)

