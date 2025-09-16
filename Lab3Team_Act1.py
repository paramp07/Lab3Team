# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, nor tolerate those who do"
# "I have not given or recieved any unauthorized aid on this assignment"
#
# Name: Param Patel
# Section: 537
# Assignment: Lab 3.1
# Date: 16 September 2025


# this will convert seconds per revolution to hertz
seconds_per_revolution = float(input("Enter time in seconds per revolution: "))
hertz = 1 / seconds_per_revolution
print(f"{seconds_per_revolution} seconds per revolution is {hertz} hertz")

# convert from miles per hour to centimeters per second

miles_per_hour = float(input("Enter speed in miles per hour: "))
centimeters_per_second = miles_per_hour * 160934.4 / 3600
print(f"{miles_per_hour} miles per hour is {centimeters_per_second} centimeters per second")

# this convert degrees fahrenheit to degrees Rankine

degrees_fahrenheit = float(input("Enter temperature in degrees Fahrenheit: "))
degrees_rankine = degrees_fahrenheit + 459.67
print(f"{degrees_fahrenheit} degrees Fahrenheit is {degrees_rankine} degrees Rankine")

