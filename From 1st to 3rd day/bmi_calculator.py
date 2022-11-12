print("Welcome to the BMI Calculator. ")
weight = float(input("What's your weight in kg? "))
height = float(input("What's your height in m? "))
bmi = round(weight / height ** 2, 2)
bmi_message = f"Your BMI is {bmi}. "
if bmi < 18.5:
  print(bmi_message + "You're underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
  print(bmi_message + " You have a normal weight.")
elif bmi > 24.9 and bmi <= 30:
  print(bmi_message + "You're overweight.")
else:
  print(bmi_message + "You're obese.")
