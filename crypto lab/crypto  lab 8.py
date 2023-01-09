# RSA
import random
p=int(input("enter first prime number:\t"))
q=int(input("enter second prime number:\t"))
n=p*q
phi=(p-1)*(q-1)
#function of gcd
def gcd(p,q):
    while q!=0:
        p,q=q,p%q
    return p
def Euler_function(x):
    if x==1:
        return 1
    else:
        phi_list=[y for y in range(1,x) if gcd(x,y)==1]
        return phi_list
#finding e relatively prime to phi(n)
for i in range(2,phi):
    e=random.choice(Euler_function(phi))
    if gcd(e,phi)==1:
        break

#defining modulur inverse
def modInverse(x,y):
    for i in range(1,y):
        if((x*i)%y==1):
            return i
    return -1
d=modInverse(e,phi)
print('public key pair=({},{})'.format(n,e))
print('private key pair=({},{})'.format(n,d))
#encryption and decryption of the message
print('value of e=',e)
M1=input('enter the message:\t')
M1=M1.upper()
cipher=""
result=""
for i in range(len(M1)):
    M=ord(M1[i])
    C=pow(M,e,n)
    cipher+=chr(C)
    M_decrypted=pow(C,d,n)
    result+=chr(M_decrypted)
print('the encrypted message:\t'+cipher)
print('the decrypted message:\t'+result)

     

