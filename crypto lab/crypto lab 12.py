#Hill cipher
import numpy as np
n=2
#k1=input('enter the  key having length {}:'.format(n*n))
#M1=input('enter the message having length multiple of {}'.format(n))
K1="Part"
M1="Banepa"
M1=M1.replace(" ","")
M1=M1.upper()
K1=K1.upper()
m=len(M1)
#encryption
K=[]
for i in range(len(K1)):
    K.append(ord(K1[i])-65)
x=np.reshape(K,(n,n)).T#list in matrix form in n,n and .T does transpose
M=[]
for i in range(m):
    M.append(ord(M1[i])-65)
    y=np.reshape(M,(n,m//n))
#multiplying key and message matrix 
c=(np.dot(x,y))%26#dot means multiply
c1=np.reshape(c+65,(1,m))
#converting  ciphertext number in  list of alphabets
c2=[]
for i in range(m):
    c2.append(chr(c1[0][i]))
print("Cipher text:\t","".join(c2))
def modInverse(x,y):
    for i in range(1,y):
        if((x*i)%y==1):
            return i
    return -1
x_det=int(np.linalg.det(x))%26
det_inv=modInverse(x_det,26)
x_adj=np.array([[x[1][1],-x[0][1],-x[1][0],x[0][0]]])
x_inv=(x_det*x_adj)%26
#multiplying   inverse key and cipher text
M_dec1=(np.dot(x_inv,c))%26
M_dec2=np.reshape(M_dec1+65,(1,m))
M_dec=[]
for i in range(m):
    M_dec.append(chr(M_dec[0][i]))
print("Cipher text:\t","".join(M_dec))
    