import time 
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for i in numbers:
        time.sleep(0.2)
        print('square',i*i)

def calc_cube(numbers):
    print("calculate cube numbers")
    for i in numbers:
        time.sleep(0.2)
        print('square',i*i*i)

array =[2,3,8,9]
t=time.time()

t1 = threading.Thread(target =calc_square ,args = (array,))
t2 = threading.Thread(target =calc_cube ,args = (array,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in  : ",time.time()-t)
print("hah....I am done with all my work now!")
