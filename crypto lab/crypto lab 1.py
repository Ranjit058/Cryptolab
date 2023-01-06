p=int(input('enter the value of prime:'))
a=int(input('enter the value whose inverse is required:'))
for i in range(1,p):
    if(i*a)%p==1:
        break
print('required multiplicative inverse of {} is {}'.format(a,i)) 
print('required additive inverse of {} is {}'.format(a,p-a))   