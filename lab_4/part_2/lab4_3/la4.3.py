

def prime(n,i,c):
    while(i<n):
        if(n%i==0):
            c=c+1
        i=i+1
    if(c==0):
        print 'prime'
    else:
        print 'not prime'
        
    
no=input()
i=2
c=0
prime(no,i,c)

