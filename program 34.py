str=input("enter a string:")
print("inputed string is:",str)
if(str.endswith("ing")):
    str=str+'ly'
else:
    str=str+'ing'
print("the formated string is:",str)