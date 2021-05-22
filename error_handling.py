def divied(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is meaningless" 

print(divied(1,5))
print("End the program")