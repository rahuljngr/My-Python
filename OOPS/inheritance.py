class Vehicle:
    def general_uses(self):
        print("general uses: Transporation")

class Car(Vehicle):
    def __init__(self):
        print ("I am a car")
        self.wheels = 4
        self.roof = True

    def specific_uses(self):
        self.general_uses()
        print("for family use")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am a motor cycle")
        self.wheel = 2
        self.roof = False
    def specific_uses(self):
        print("for single use")

c = Car()
c.specific_uses()

m =MotorCycle()
m.general_uses()
m.specific_uses()
