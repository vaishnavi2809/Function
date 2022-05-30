def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutting aborted"
    else:
        return "Sorry"
str=input("Enter the String")
print(shut_down(str))
