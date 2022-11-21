list1 = []
list2 = []

with open("file1.txt") as file:
  list1 = file.readlines()
  for i in range(0, len(list1)):
    list1[i] = int(list1[i].strip())
with open("file2.txt") as file:
  list2 = file.readlines()
  for i in range(0, len(list2)):
    list2[i] = int(list2[i].strip())
result = [value for value in list1 if value in list2]    
    
  

print(result)
