def febo(a,b,n):
    print a,b
    while(n!=0):
        c=a+b
        print c
        a=b
        b=c
        n=n-1
        
a,b=input('enter two number')
n=input('enter the range')
febo(a,b,n)
