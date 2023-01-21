class Value:
    def __init__(self):
        self.value=[]
    def append(self,element):
        self.value.append(element)
    def __str__(self):
        return self.value
v1=Value()
f=open("input.txt","w")
f.write("97\n102\n116\n99\n95")
f=open("input.txt","r")
for line in f:
    line=line.rstrip("\n")
    v1.append(line)
print(v1.__str__())


    