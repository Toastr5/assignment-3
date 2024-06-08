book_quant = int(input("Enter the quantity of book purchased: "))
unit_cost = float(input("Enter unit quantity: "))
total_cost = book_quant * unit_cost
if total_cost > 50:
  shipping = 0
  print(f"Since your total is over $50.00 shipping is free" 
  f" and your total is only ${total_cost}")
else: 
  shipping = 50
  print(f"Since your total is under $50.00 shipping is $50.00" 
  f" and your total is ${total_cost + shipping}")