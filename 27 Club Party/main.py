names = []
invitation = []
username = "(name)"

with open("names/names.txt") as file:
  names = file.readlines()
  for i in range(0, len(names)):
    names[i] = names[i].strip()

with open("sample/invitation.txt") as file:
  invitation = file.read()

filenames = []
for i in range(0, len(names)):
  filenames.append(names[i] + ".txt")
  
for i in range(0, len(names)):
  new_invitation = invitation.replace(username, names[i])
  with open(filenames[i], "w") as file:
    file.write(new_invitation)
  
  
  
