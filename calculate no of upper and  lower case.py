# : Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def count(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
        else:
            pass
    print("Uppercase letters are :",u)
    print("Lowercase letters are :",l)
str=input("Enter string")
count(str)
