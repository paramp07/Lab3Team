# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, nor tolerate those who do"
# "I have not given or recieved any unauthorized aid on this assignment"
#
# Name: Param Patel
# Section: 537
# Assignment: Lab 3.2
# Date: 16 September 2025

# intialize variables
time1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position at time 1: "))
y1 = float(input("Enter the y position at time 1: "))
z1 = float(input("Enter the z position at time 1: "))
time2 = float(input("Enter the second time: "))
x2 = float(input("Enter the x position at time 2: "))
y2 = float(input("Enter the y position at time 2: "))
z2 = float(input("Enter the z position at time 2: "))

# calculate the time intervals
time_interval = (time2 - time1) / 4

# calculate the positions at the different times with a for loop

for i in range(0, 5):
    # calculate the current time by addin the time1 with the time interval multiplied by the loop index
    current_time = time1 + i * time_interval

    # calculate interpolation factor
    t = (current_time - time1) / (time2 - time1) 

    # calculate the x, y, and z positions using linear interpolation formula
    x_position = x1 + (x2 - x1) * t
    y_position = y1 + (y2 - y1) * t
    z_position = z1 + (z2 - z1) * t
    #print current time and interpolated positions with specified formatting and decimal places.
    print(f"At time {current_time:.1f} seconds, the object is at ({x_position:.2f}, {y_position:.2f}, {z_position:.2f})")
