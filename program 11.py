def change_char(str1):
 char=str1[0]
 str1=str1.replace(char,'$')
 str1=char+str1[1:]
 return str1
str=input("Enter the string:")
print("the original string:",str)
print("the replaced string:",change_char(str))