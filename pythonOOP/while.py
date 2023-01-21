y=0
x=y+5
loopnumber=1
while( x > y ):
    print("(",loopnumber,")")
    loopnumber+=1
    print("x=>",x)
    print("y=>",y)
    print(x,"is greater than",y)
    x-=1
    
if( x == y ):
    print("they are equal")
