import random
def add_random_alphabets(string):
# Generate 3 random lowercase alphabets
    random_prefix = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
    random_suffix = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
    
    # Concatenate the random alphabets with the string
    new_string = random_prefix + string + random_suffix
    return new_string
q=input("enter your choice  ")
if(q=='encode'):
    x=input("enter your message:    ")
    y=x.split()
    # print(y)
    z=[]
    for i in range(0,len(y)):
        if(len(y[i])<4):
            z.append(y[i][::-1])
        else:
            c=y[i][0]
            # print(c)
            a=y[i][1:]
            # print(a)
            b=a+c
            # print(b)
            z.append(add_random_alphabets(b))

    last =" ".join(z)

    # print(z)
    print(last)

# encoding done
elif(q=="decode"):
    r=input("enter a message to decode: ")
    lastlist=r.split()
    # print(lastlist)
    l=[]
    for i in range(0,len(lastlist)):
        if(len(lastlist[i])<4):
            l.append(lastlist[i][::-1])
        else:
            m=lastlist[i][3:len(lastlist[i])-3]
            n=m[-1]
            # print(n)
            o=n+m[0:len(m)-1]
            # print(o)
            l.append(o)
    print(" ".join(l))
else:
    print("enter valid command")