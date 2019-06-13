class rect:
    def area(self,l,b):
        self.A=l*b
    def peri(self,l,b):
        self.P=2*(l+b)
    def display(self):
        print self.A
        print self.P
l,b=input()
ob=rect()
ob.area(l,b)
ob.peri(l,b)
ob.display()
