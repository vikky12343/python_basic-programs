class power:
    def __init__(self,a,b):
        self.x=a
        self.n=b
        self.p=1
    def pow(self):
        while(self.n>0):
            self.p=self.p*self.x
            self.n=self.n-1
    def display(self):
        print self.p
a,b=input()
ob=power(a,b)
ob.pow()
ob.display()
