# Author: Divyang Parikh
# Date: 10/30/25
# Problem 3 – Pick and print a random day of the week

import random  # Import random module to select random elements

# Create a list of all days in a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

random_day = random.choice(days) #pick a random item from list

print("Random day of the week:", random_day) #print the selected day