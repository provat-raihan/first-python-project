def new(x):
    if(x==0):
        return 0
    return new(x-1) + x
print(new(7))