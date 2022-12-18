list=[]
n=int(input("enter the limit of list:"))
for i in range(0,n):
    print("enter the number",i+1,".")
    num=int(input())
    if(num<100):
        list.append(num)
    else:
        list.append("over")
print(list)