def is_leap(year):
  if year % 4 == 0:
  
    if year % 100 == 0:
    
      if year % 400 == 0:
         return True
      else:
        return False
  
    else:
      return True
  
  else:
    return False
def days_in_month(year, month):
  if is_leap(year) == True and month == "February":
    print(f"{month} of  {year} has {days_in_months[month]+1} days.")
  else:
    print(f"{month} of  {year} has {days_in_months[month]} days.")
    
days_in_months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,"July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
year = int(input("Choose a year: "))
month = input("Choose a month: ")
days_in_month(year, month)

  
