#Will you be able to buy a house with all your salary 5 years later?
def increaseSalary(salary):
    year=2 # In the first year, the first entered salary will add up.
    total=salary*12
    while(year<6):
        salary*=1.1 # %10 increase for salary every year.
        total+=salary*12
        year+=1
    return total
def housePrice(price):
    year=2 # The price entered in the first year will be valid.
    while(year<6):
        price*=1.5 # %50 increase for house price every year.
        year+=1
    return price
salary=int(input("Enter your salary=> "))
total=0
total=increaseSalary(salary)
price=int(input("Enter the house price=> "))
price=housePrice(price)
if(total>price):
    increasingMoney=total-price
    print("Congratulations you can buy the house.")
    print("İncreasing Money={}$".format(int(increasingMoney)))
elif(total==price):
    print("Congratulations you can buy the house.")
    print("Your money is equal to the price of the house.")
else:
    requiredMoney=price-total
    print("Sorry you can't buy the house")
    print("Required Money={}$".format(int(requiredMoney)))
    
    
    
    
    
    
    


