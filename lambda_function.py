'''def devide(a,b):
    return a/b

print(devide(10,3))'''

'''devide = lambda a,b: a/b
print(devide(10,3))'''


def a_fist(list1):
    return list1[0]
list1 = [[1,13],[4,3],[5,46]]
list1.sort(key=a_fist)
print(list1)

list1.sort(key=lambda x:x[1])
print(list1)