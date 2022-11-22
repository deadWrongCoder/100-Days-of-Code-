sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list = sentence.split(" ")

result = {item:len(item) for item in list}

print(result)
