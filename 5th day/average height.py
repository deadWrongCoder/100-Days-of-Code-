heights = [162, 170, 185, 174, 173, 181]
sum = 0
for height in heights:
  sum += height
print(f"Average height is {round(sum/len(heights), 2)}")  
