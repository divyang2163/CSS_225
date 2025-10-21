#Author: Divyang Parikh
#Date: 10/19/25
str_time = input("What time is it now? ")                              #Asking user for current time and wait hours
str_wait_time = input("What is the number of hours to wait? ")

time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_goes_off = (time + wait_time) % 24                       #Calculating time and printing statement
print("The alarm will go off at:", time_when_alarm_goes_off)
