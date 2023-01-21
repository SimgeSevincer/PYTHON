#append
#remove
#pop
def read():
    list=[]
    for number in range(2):
        x=int(input("x=> "))
        list.append(x)
    return(list)
def sum(result):
    total=0
    for item in result:
        total+=item
    return total
def display(totallist):
    print("total=",totallist)
result=read()
totallist=sum(result)
display(totallist)