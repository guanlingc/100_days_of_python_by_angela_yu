# Tip calculator
print(f'Welcome to the tip calculator!')
bill = int(input("How much was the bill? $"))
tips = int(input("How much tips was given? 10%, 12% 15% "))
people = int(input("How many people are splitting the tips? "))

total_tip = bill * (tips/100)
bill_per_pax = (bill + total_tip) / people

print(f"Tips is ${round(total_tip,2)}, making the total bill ${round(bill+total_tip,2)}")
print(f"The amount that each person has to pay is ${round(bill_per_pax,2)}")
print(f'Thank you!!')
