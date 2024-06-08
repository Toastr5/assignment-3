name = str(input("Enter your last name: "))
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))
adjusted_gross_income = gross_income - (dependents * 12000)
if adjusted_gross_income > 50000: 
  tax_rate = 0.2
else: 
  tax_rate = .1
income_tax = round(adjusted_gross_income * tax_rate, 2)
if income_tax <= 0.0: 
  income_tax = 100.0
print(f"{name} with a gross income of ${gross_income} and {dependents} dependents"
     f" has an adjusted income of ${adjusted_gross_income}"
      f" and owes ${income_tax} in income tax")