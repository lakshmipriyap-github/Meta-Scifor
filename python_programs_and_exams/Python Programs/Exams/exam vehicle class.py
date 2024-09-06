'''
TASK2- Vehicle Problem:
In a town, a garage owner manages cars and motorcycles. The owner
needs a program to track vehicle operations. Cars honk when started;
motorcycles pop wheelies when started. The owner wants to start and
stop vehicles as requested. Instructions for the code: Create a Python
program with classes for Vehicle, Car, and Motorcycle as shown. Define
attributes and methods for starting and stopping vehicles. Create
instances of Car and Motorcycle. Demonstrate starting, performing
vehicle-specific actions, and stopping both instances. Ensure the
program runs without errors and showcases vehicle functionalities.
'''
class Vehicle:
    def __init__(self):
        self.start = "Vehicle start"
        self.stop = "Vehicle stop"
    def startVehicle(self):
        print("The Vehicle starts:",self.start)
        return
    def stopVehicle(self):
        print("The Vehicle stops:", self.stop)
        return

class Car(Vehicle):
    def startVehicle(self):
        self.start = "honk"
        print("The car starts:",self.start)
        return
    def stopVehicle(self):
        self.stop = "honk stopped"
        print("The car stops:", self.stop)
        return

class Motorcycle(Vehicle):
    def startVehicle(self):
        self.start = "pop the wheels"
        print("The Motorcycle starts:",self.start)
        return
    def stopVehicle(self):
        self.stop = "popping of wheel stopped"
        print("The Motorcycle stops:", self.stop)
        return

carObj = Car()
carObj.startVehicle()
carObj.stopVehicle()

motObj = Motorcycle()
motObj.startVehicle()
motObj.stopVehicle()