str=input("enter string")
count=0
for i in str:
    if i in'aeiouAEIOU':
        count+=1
print("number of vowels is",count)