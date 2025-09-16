# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, nor tolerate those who do"
# "I have not given or recieved any unauthorized aid on this assignment"
#
# Name: Param Patel
# Section: 537
# Assignment: Lab 1.2
# Date: 07 September 2025


import math

print("This shows the evaluation of (1+1/x)^x")

x_values = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]

print("Evaluating (1+1/x)^x")
for x in x_values:
    print((1+1/x)**x)