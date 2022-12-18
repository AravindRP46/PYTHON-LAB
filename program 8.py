def print_factor(x):
    print("the factors of",x,"are")
    for i in range(1,x+1):
        if(x%i==0):
            print(i)
num=int(input("enter the number to find factor"))
print_factor(num)