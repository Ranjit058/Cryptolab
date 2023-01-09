#
impot random

q=int(input("enter second prime number:\t"))
a=int(input("enter primitive root of q:\t"))
XA=int(input("enter alice secret key(XA):\t"))
def modInverse(x,y):
    for i in range(1,y):
        if((x*i)%y==1):
            return i
    return -1