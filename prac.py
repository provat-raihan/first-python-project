x=input("subject name1: ")
y=input("subject name2: ")
z=input("subject name3: ")
m=int (input("subject marks1: "))
n=int (input("subject marks2: "))
o=int (input("subject marks3: "))

dic={}
dic.update({"x":m})
dic.update({"y":n})
dic.update({"z":o})
print(dic)