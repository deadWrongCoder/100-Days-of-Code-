def add(a1, a2):
  return a1 + a2
def sub(a1, a2):
  return a1 - a2
def mul(a1, a2):
  return a1 * a2
def div(a1, a2):
  return a1 / a2
def calculation():
  num1 = float(input("Write the first number to start calculating: "))
  new_operation = input("Choose an operation: ")
  num2 = float(input("Write another number: "))
  function = operation[new_operation]
  result = function(num1, num2)
  print(f"Result is {result} ")
  ending_calculation = False
  while not ending_calculation:
    answer = input("Do you want to continue calculation with the result or start new calculation? Type Y or N ").upper()
    if answer == "N":
      calculation()
    else:
      new_operation = input("Choose an operation: ")
    num2 = float(input("Write another number: "))
    function = operation[new_operation]
    result = function(result, num2)
    print(f"Result is {result} ")
        
operation = {"+": add, "-": sub, "*": mul, "/": div}
calculation()
