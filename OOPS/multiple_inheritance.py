class Father:
    def skills(self):
        print("gardening,programming")

class Mother:
    def skills(self):
        print("cooking, teaching")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("cricket")

rahul = Child()
rahul.skills()