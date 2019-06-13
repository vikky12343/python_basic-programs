def compound(p,n,r):
    ci=p*((1+r/100.0)**n-1)
    return ci
p,n,r=input()
z=compound(p,n,r)
print z 
