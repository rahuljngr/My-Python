list1 = [220,452,748,150]
'''list2 = []

for list in list1:
    list2.append(list/10)
print(list2)

'''


#list comprehension
list2 = [list/10 for list in list1]

print(list2)