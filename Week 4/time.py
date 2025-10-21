#Author: Divyang Parikh
#Date: 10/19/25
current_time_str = input("What is the current time (in hours 0-23)? ")          #Asking user for time and wait time
wait_time_str = input("How many hours do you want to wait? ")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = (current_time_int + wait_time_int) % 24                       #Calculating time after current hours added with wait time
print("The time after waiting will be:", final_time_int)
