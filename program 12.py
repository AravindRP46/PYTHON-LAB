def character_exchange(str1):
    str2=(str1[-1:]+str1[1:+-1]+str1[:1])
    return str2
str=input("enter the string:")
print("the original string:",str)
print("string after swapping first and last character:",character_exchange(str))
