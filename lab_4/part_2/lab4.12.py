def pal(s):
    str=''
    for i in s:
        str=i+str
    if s==str:
        print 'true'
    else:
        print 'false'
        
s=input()
pal(s)
