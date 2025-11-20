# Divyang Parikh
# 11/20/2025
# Problem 4: Count from 0 to 50. If divisible by 10, add to list 'tens'

tens = []          # list for numbers divisible by 10
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("Numbers divisible by 10:", tens)
