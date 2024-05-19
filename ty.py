a = input("Enter the value butween 5 and 9: ")

if (a == "quit"):
    print("ohk")
b=int(a)
print(type(b))
try:
    if(b < 5 or b > 9):
        raise ValueError("The number should be between 5 and 9")
except:
    if(b is not int):
        raise TypeError("this is a string")



