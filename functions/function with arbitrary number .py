# non-key arguments
def mean(*args) :
    return args


print(mean(1,23,25))

#keyword arguments

def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))