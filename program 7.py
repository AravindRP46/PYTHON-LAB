n=int(input("enter the limit"))
n=int(n)
B,i=1,1
print("the perfect square up to",n,"is")
for i in range(B,n):
    P=B*B
    B=B+1
    if(P<n):
        print(P)