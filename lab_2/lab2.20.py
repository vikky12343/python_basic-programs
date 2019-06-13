a,b=input()
i=1
if(a>b):
    min=b
else:
    min=a
while(i<=min):
    if(a%i==0 and b%i==0):
        gcd=i
    i=i+1
print gcd
