names = []
invitation = []
username = "(name)"

with open("names/names.txt") as file:
  names = file.readlines()


with open("sample/invitation.txt") as file:
  invitation = file.readlines()

filenames = []
for i in range(0, len(names)):
  filenames.append(names[i] + ".txt")
  
for i in range(0, len(names)):
  invitation[0] = invitation[0].replace(username, names[0])
  

  with open(filenames[i], "w") as file:
    file.write(" ".join(invitation))
  
