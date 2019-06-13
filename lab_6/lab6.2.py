class power:
    p=1
    def fun(self,x,n):
        for self.i in range(1,n+1):
            self.p=self.p*x
    def display(self):
        print self.p
x,n=input()
ob=power()
ob.fun(x,n)
ob.display()
