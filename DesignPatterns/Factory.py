class Car:
    def drive(self):
        print("Driving Car")

class Bike:
    def drive(self):
        print("Driving Bike")

class VehicleFactory:
    def getVehicle(self, type):
        if type == "car":
            return Car()
        return Bike()

obj = VehicleFactory()
v = obj.getVehicle("car")
v.drive()