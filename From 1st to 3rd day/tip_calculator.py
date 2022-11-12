print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? "))
number = int(input("How many people to split the bill? "))
tip = int(input("How much tip would you like to give? "))
result = (total_bill * (tip/100) + total_bill) / number
print(f"You need to pay {result}")
