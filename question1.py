quantity = int(input("Enter the quantity of the item: "))
if quantity < 1000: 
  price = quantity * 5 
  unit_price = 5
else: 
  price = quantity *3
  unit_price = 3
tax = round(price * .07,2)
total = round(price + tax,2)
print(F"The total price of {quantity} items is ${total}"
    f" with a tax of ${tax} and a unit price of ${unit_price}")