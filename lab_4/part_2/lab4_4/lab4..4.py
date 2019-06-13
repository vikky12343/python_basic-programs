def prime(a,b):
    while a<=b:
        c=0
        if(a==2 or a==3 or a==5 or a==7):
            c=1
        elif(a%2==0 or a%3==0 or a%5==0 or a%7==0):
            c=0
        else:
            c=1
        if(c==1 and a!=1):
            print a
        a=a+1
    return 0
a,b=input()
prime(a,b)
