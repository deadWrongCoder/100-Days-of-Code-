heights = input("What are heights? ").split(", ")
sum = 0
for n in range(0, len(heights)):
  heights[n] = int(heights[n])
for height in heights:
  sum += height
print(f"Average height is {round(sum/len(heights), 2)}")  
