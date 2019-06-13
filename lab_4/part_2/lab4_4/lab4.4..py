a,b=input()
while(a<=b):
    c=0
    i=2
    while(i<a):
        if(a%i==0):
            c=c+1
        i=i+1
    if(c==0 and a!=1):
        print a
    a=a+1
        
            
        
    
