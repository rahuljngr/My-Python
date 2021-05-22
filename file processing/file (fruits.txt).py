myfile = open("/home/rahul/python3/file processing/fruits.txt")
read_file = myfile.read()
myfile.close()
print(read_file)

with open("/home/rahul/python3/file processing/fruits.txt") as myfile:
    read_file = myfile.read()

print(read_file)


