class publisher:
    def __init__(self,n):
        self.name=n
class book(publisher):
    def __init__(self,n,t,a):
        super().__init__(n)
        self.title=t
        self.author=a
class python(book):
    def __init__(self,n,t,a,p,pgs):
        super().__init__(n,t,a)
        self.price=p
        self.pages=pgs
    def display(self):
        print(p1.name)
        print(p1.title)
        print(p1.author)
        print(p1.price)
        print(p1.pages)
p1=python("python","introduction to python","jeeva jose",450,300)
p1.display()