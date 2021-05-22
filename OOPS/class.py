class  Human:
    def __init__(self, n , o):
        self.name = n
        self.occupation = o

    def Do_work(self):
        if self.occupation == "tennis player":
            print (self.name,"play tennis")
        elif self.occupation =="actor":
            print(self.name,"shoot film")
    
    def  speaks(self):
        if self.occupation == "tennis player":
            print (self.name,"speaks English")
        elif self.occupation =="actor":
            print(self.name,"speaks Hindi")

tom = Human("tom cruse", "actor")
tom.Do_work()
tom.speaks()

maria = Human("maria sarapova","tennis player")
maria.Do_work()
maria.speaks()