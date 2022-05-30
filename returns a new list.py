def unique(lst):
    a=[]
    for i in lst:
        if i not in a:
            a.append(i)
        else:
            pass
    return a
list=eval(input("Enter the List"))
print(unique(list))
