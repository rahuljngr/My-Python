class Employee:
    increment = 1.5
    no_of_employees =0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1
        #self.increment = 1.4
    def increase(self):
        self.salary = int(self.salary * Employee.increment) 
    @classmethod
    def change_increment(cls,amount):
        cls.increment =amount  
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("/")
        return cls(fname,lname,salary)

    @staticmethod
    def isopen(day):
        if day =='monday':
            return False
        else:
            return True 

    def __add__(self,other):
        return self.salary + other.salary
    
    def __repr__(self):
        return "Employee({},{},{})".format(self.fname,self.lname,self.salary)
rahul = Employee("rahul","jangir",55000)
sonu = Employee("sonu","choyal",2000)

print(rahul)