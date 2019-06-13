#area of rectangular prism=2(wl+hl+hw)
def area(l,h,w):
    a=2*(w*l+h*l+h*w)
    return a
l,h,w=input()
A=area(l,h,w)
print A
