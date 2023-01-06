t1=0
t2=1
t=1
b=int(input('enter the value for inverse:'))
n=int(input('enter the modular value (n)'))
r1=n
r2=b
while(t!=0):
    q=r1//r2
    r=r1%r2
    t=t1-q*t2
    if t<0:
        t=t+n
    else:
        t=t%n
    print('{}      {}      {}      {}      {}      {}      {}'.format(q,r1,r2,r,t1,t2,t)) 
    r1=r2; r2=r; t1=t2; t2=t
print('the inverse of {} mod({})= {}'.format(b,n,t1))    
