def readLine():
    list1=[]
    f=open("fileelist.txt","r")
    for line in f:
        list1.append(line)
    return(list1)
list=readLine()
for x in list:
    print(x)
#csb excel..dataların birbirinde virgülle ayrıldığı dosya