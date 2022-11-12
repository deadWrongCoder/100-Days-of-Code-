print("Welcome to Life in Weeks! ")
age = int(input("What's your age? "))
years_left = 70 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"We assume you live up to 70 years. So you've {years_left} years, {months_left} months, {weeks_left} weeks, {days_left} days left.")
