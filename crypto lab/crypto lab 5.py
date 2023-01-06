#Miller Robins prime test
n=int(input("enter number for MIller Rabin primilary test:\t"))
if n<=3:
    print("input must be greater than 3.")
    n=int(input("enter number for MIller Rabin primilary test:\t"))
elif n%2==0:
    print("{} is a composite number".format(n))
s,d=0,n-1
while d%2==0:
    s=s+1
    d=d//2
a=int(input("enter the  value of a less than n:\t"))
x=pow(a,d,n)#a^n(mod n)
if x==1 or x==n-1:
    print('{} is a prime number'.format(n))
for _ in range(s-1):
    x=pow(x,2,n)
    if x==n-1:
        print('{} is a prime number.'.format(n))
        break