s=int(input("enter start year:"))
e=int(input("enter end year:"))
if(s<e):
    print("leap years are:",end="")
    for i in range(s,e):
        if i%4==0 and i%100!=0:
            print(i,end=" ")
else:
    print("invalid")