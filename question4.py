name = str(input("Enter the name of the appliance: "))
price = float(input("Enter the price of the appliance: "))
if price > 1000:
  warrenty = price *.1
  print(f"For a {name} costing {price} the warrenty costs ${warrenty}"
  f" for a final total of ${price + warrenty}")
else:
  warrenty = price *.05
  print(f"For a {name} costing ${price} the warrenty cost ${warrenty}"
    f" for a final total of ${price + warrenty}")