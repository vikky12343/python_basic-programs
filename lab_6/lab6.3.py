class circle:
    def __init__(self,rd):
        self.r=rd
    def area(self):
        self.A=3.14*self.r*self.r
    def peri(self):
        self.P=2*3.14*self.r
    def display(self):
        print self.A
        print self.P
r=input()
ob=circle(r)
ob.area()
ob.peri()
ob.display()
