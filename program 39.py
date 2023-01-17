class rect:
    def __init__(self,l,b):
        self.length=l
        self.width=b
    def findArea(self):
        b=(self.length * self.width)
        return b
    def findPerimeter(self):
        c=2*(self.length+self.width)
        return c
a1=rect(10,3)
a2=rect(1,3)
print(a1.findArea())
print(a1.findPerimeter())
if a1.findArea()>a2.findArea():
    print("a1 is greater")
else:
    prinr("a2 is greater")