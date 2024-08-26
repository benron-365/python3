# Given height in cm ,print that length in inches and feet. 

# Get user input
height_cm = float(input("Enter height in centimeters: "))

# Convert height from centimeters to inches
length_inches =  height_cm / 2.54

# Convert length from inches to feet
length_feet = height_cm / 30.48

# Print the results
print(f"Lenght in Inches: {length_inches:.2f}")
print(f"Length in feet: {length_feet:.2f}")


# Here's how the program works:

# 1. It asks the user to enter their height in centimeters and length in inches.
# 2. It converts the height from centimeters to inches by dividing by 2.54 (since 1 inch = 2.54 cm).
# 3. It converts the length from centimeters to feet by dividing by 30.48 (since 1 foot = 30.48 cm).
# 4. It prints the results to two decimal places using the :.2f format specifier.

# Note: This program assumes that the user will enter valid numeric input. You may want to add error handling to handle cases where the user enters something other than a number.