message = input("Write a message: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_message = ""
for char in message:
  if char in alphabet:
    end_message += alphabet[alphabet.index(char) + 1]
  else:
    end_message += char
print(end_message)  
