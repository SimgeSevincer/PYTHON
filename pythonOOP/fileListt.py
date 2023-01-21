def readLine():
    lines=""
    f=open("fileList.txt","r")
    for line in f:
        lines+=line
    return(lines)
lines=readLine()
f=open("fileList.txt","r")
list=[]
for item in f:
    list.append(item)
for x in list:
    print(x)

