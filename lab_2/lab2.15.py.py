n=input('enter  number')
i=0
while(n>0):
    p=n%10
    if(p==9):
        p=0
    k[i]=p
    i=i+1
    n=n/10
print k
    
