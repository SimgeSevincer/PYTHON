def read(n):
    name = []
    for i in range(n):
        name.append((input("Enter name => ")))
    return(name)
def length(name1,n):
    for a in range(n):
        b=a+1
        for b in range(n):
            if(len(name1[a])<len(name1[b])):
                nullpacket=name1[a]
                name1[a]=name1[b]
                name1[b]=nullpacket
    return(name1)
n=int(input("Enter number of names"))
name1=[]
name1=read(n)
name1=length(name1,n)
print(name1)
    


