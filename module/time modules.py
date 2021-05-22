import time

while True:
    with open("vegetables.txt") as file:
        print(file.read())
        time.sleep(5)