with open("vegetables.txt" ,'w') as myfile :
    myfile.write("Tomato \nonion \nlady finger")
    myfile.write("\nGralic")


#read and write both
with open("vegetables.txt", 'a+') as myfile:
    myfile.write("\nokra")
    myfile.seek(0) # use fot the curser in start point
    contant = myfile.read()

print(contant)