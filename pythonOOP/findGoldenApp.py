def bag1():
    print("5 items, including one gold, are thrown into the bag by the audience for first competitor.")
    baglist1=[]
    for i in range(4):
        item=input(("Please enter the name of the items => "))
        baglist1.append(item)
    return baglist1
    
def bag2():
    print("5 items, including one gold, are thrown into the bag by the audience for second competitor.")
    baglist2=[]
    for i in range(4):
        item=input(("Please enter the name of the items => "))
        baglist2.append(item)
    return baglist2
def findgolden1(baglist1):
    item=""
    item=int(input("First contestant please start entering numbers for the first bag"))
    while(baglist1[item]!="golden"):
        item=input("First contestant please start entering numbers for the first bag")
    return item 
    
print("Welcome to Competition of Find Golden")
competitor1=input("Please enter first competitor name => ")
competitor2=input("Please enter second competitor name => ")
baglist1=bag1()
baglist2=bag2()
print("Let both contestants start pulling items from their own bags")
findgolden1(baglist1)