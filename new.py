a=input('Enter a number between 5 and 9: ')
if (a=='quit'):
    exit()
elif a.isalpha():
    print('Enter an integer value')
elif ((int(a)<5) or (int(a)>9) ):
    raise ValueError('Entered value is not in between 5 or 9')
elif((int(a)>=5) or (int(a)<=9) ):
    print ('Thank you for you input')