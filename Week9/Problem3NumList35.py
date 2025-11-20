# Divyang Parikh
# 11/20/2025
# Problem 3: Keep asking user for numbers, append to a list, stop when sum > 100

numbers = []              # to store entered numbers
total = 0                 # running sum

while total <= 100:
    num = int(input("Enter a number: "))
    numbers.append(num)
    total += num          # update the sum

print("Numbers entered:", numbers)
print("Total sum:", total)
