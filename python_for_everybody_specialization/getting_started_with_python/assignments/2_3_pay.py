'''

Assignment 2.3
Write a program to prompt the user for hours and rate per hour 
using input to compute gross pay. Use 35 hours and a rate of 2.75 
per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the 
string to a number. Do not worry about error checking or bad user data.

'''

hours = input('Enter Hours:')
rate_per_hour = input ('Enter Rate per Hour:')
#   Output expect to be in a numeric float format
pay = float(hours) * float(rate_per_hour)
print('Pay:',pay)
#  print('Pay: ' + str(pay)) is another option
