str=input("enter the string to check:")
i=0
s=0
k=len(str)
for j in range(k-1,-1,-1):
    if(str[i]!=str[j]):
        s=1
        break
    i=i+1
if(s==0):
    print("the given string",str,"is palindrome")
else:
    print("the given string",str,"is not palidrome")