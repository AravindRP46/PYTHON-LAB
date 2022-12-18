num=int(input("enter the number to find factorial"))
factorial=1
if(num<0):
    print("sorry factorial does not exist for negative number")
elif(num==0):
    print("factorial of 0 is 1 ")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("the factorial of the given number",num,"is",factorial)