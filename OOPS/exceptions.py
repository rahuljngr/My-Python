x = input("Enter Number1: ")
y = input("Enter Number2: ")
try:
    z= x / int(y)
except ZeroDivisionError as e:
    print(e)
    z=None
except TypeError as e:
    print(type(e).__name__) # find Exception type name
    z=None
print("Divison is: ",z)