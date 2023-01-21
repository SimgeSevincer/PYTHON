def bigger(c1,c2):
    if(c1>c2):
        return (c1)
    if(c2>c1):
        return (c2)
def display(bigger):
    if(bigger==c1):
        print("\'",chr(c1),"\'","is greater than","\'",chr(c2),"\'")
    if(bigger==c2):
        print("\'",chr(c2),"\'","is greater than","\'",chr(c1),"\'")
c1=input("c1=> ")
c2=input("c2=> ")
c1=ord(c1)
c2=ord(c2)
bigger=bigger(c1,c2)
display(bigger)

