#Euler's totient(Phi) function
def gcd(p,q):
    while q!=0:
        p,q=q,p%q
    return p
x=int(input("Enter the number for totient function:\t"))
phi=[]
for y in range(2,x):
    if gcd(x,y)==1:
        phi.append(y)
print("The value opf euler's totient={}".format(len(phi)))
#print(phi)
