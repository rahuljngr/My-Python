def funargs (normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nhere is some lines for kwargs:")
    for key,value in kwargs.items():
        print (f"{key} is a {value}")
        

rahul = ["rahul","sonu","vikash","deepak","rajesh"]
normal="hey... we are frinds!"
rahul1 = {"rahul":"student","deepak":"teacher","sonu":"designer"}

print(funargs(normal,*rahul,**rahul1))
