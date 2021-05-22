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

class Programmer(Employee):
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,lname,salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * Employee.increment+0.2)    
        
rahul = Programmer('rahul','jangir',44000,"Python","5 years")
lovish = Employee.from_str("lovish/jackson/76000")
sonu = Employee('sonu','sharma',74000)

rahul.increase()
print(rahul.salary)
#print(rahul.salary)
#Employee.change_increment(3)
#rahul.increase()
#print(rahul.salary)