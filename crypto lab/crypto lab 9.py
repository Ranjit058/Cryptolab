#
import random

q=int(input("enter prime number:\t"))
a=int(input("enter primitive root of q:\t"))
XA=int(input("enter alice secret key(XA):\t"))
M1=input('enter the message:\t')
M1=M1.upper()
def modInverse(x,y):
    for i in range(1,y):
        if((x*i)%y==1):
            return i
    return -1

cipher1=""
cipher2=""
result=""
for i in range(len(M1)):
    M=ord(M1[i])
#alice computes ya for public
    YA=pow(a,XA,q)
#bobs encryption
    k=random.randint(2,q-1)
    KB=pow(YA,k,q)
    c1=pow(a,k,q)
    cipher1+=chr(c1)
    c2=(KB*M)%q
    cipher2+=chr(c2)
#Alices drcryption
    KA=pow(c1,XA,q)
    KA_inv=modInverse(KA,q)
    MA=(c2*KA_inv)%q
    result+=chr(MA)
print("The encrypted message pair:\t"+(cipher1+cipher2))
print("The decrypted message:\t"+result)
    