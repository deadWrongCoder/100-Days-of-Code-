year = int(input("Choose an year: "))
if year % 4 == 0:
  
  if year % 100 == 0:
    
    if year % 400 == 0:
       print(f"{year} is a leap year.")
    else:
      print(f"{year} is a common year.")
  
  else:
    print(f"{year} is a leap year.")
  
else:
  print(f"{year} is a common year.")
