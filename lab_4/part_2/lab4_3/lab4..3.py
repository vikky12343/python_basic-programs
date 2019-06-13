
def prime(n):
    if(n==2 or n==3 or n==5 or n==7):
        return 1;
    elif(n%2==0 or n%3==0 or n%5==0 or n%7==0):
        return 0;
    else:
        return 1
n=input('enter a number')
check=prime(n)
print check

    
            
