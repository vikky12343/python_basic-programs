n=input()
c=0
i=2
while(i<n):
    if n%i==0:
        c=c+1
    i=i+1
if c==0:
    print 'prime'
else:
    print 'not prime'
    
