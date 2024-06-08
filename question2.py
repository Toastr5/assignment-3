#user initial input auto capitalize
item = str(input("Enter the item: ")).capitalize()
#testing to make sure that they entered A or B. If it's not repeat the question
while True: 
  if item != "A" and item != "B":
    print("please enter item A or B")
    item = str(input("Enter the item: ")).capitalize()
#If it is A or B then break out of the loop and ask for quanitity
  else: 
    quantity = int(input("Enter the quantity of the item: "))
#If A then multiply by 10 else multiply by B becuase we already ensured it was A or B
    unit_price = round(quantity * 10, 2) if item == "A" else round(quantity * 20, 2)
#print results
    print(f"The total price of {quantity} {item} items is ${unit_price}")
    break