def mean(value):
    #if type(value) == dict :      "as same like"        if isinstance(value ,dict):
    if isinstance(value ,dict):
        new_mean = sum (value.values()) /len (value)
    else :
        new_mean = sum(value) / len(value)
    return (new_mean)
new_dict = {'rahul' : 45, 'sonu' : 25, 'deepak' : 74}
new_list = [4,21,5,265,45,22,88]

print('mean of dict : ',mean(new_dict))
print('mean of list : ',mean(new_list))


