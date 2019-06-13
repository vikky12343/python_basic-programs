def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c
a,b,c=input()
z=max(a,b,c)
print z
