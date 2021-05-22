list1 = [4,2,1,5,8,9,6,2,7,3,2]

evens = list(filter(lambda x : x %2==0,list1))

print(evens)

double = list(map(lambda y: y*2,evens))
print(double)