a=int(input("input an integer"))
n1=int("%s"%a)
n2=int("%s%s"%(a,a))
n3=int("%s%s%s"%(a,a,a))
print("n=",n1,"\n","nn=",n2,"\n","nnn=",n3)
print("sum(n+nn+nnn)=",(n1+n2+n3))