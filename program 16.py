n=int(input("enter the step size"))
print("the pyramid for the given size ",n,"is:\n")
for i in range (1,n+1):
    k=i
    for j in range(1,i+1):
        print(k,end=" ")
        k+=i
    print("")