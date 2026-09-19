# CIRCULAR GARDEN
# DATE: SEPTEMBER 19, 2026

# IMPORT THE MATH LIBRARY SO THAT WE CAN USE PREDEFINED FUNCTIONS SMOOTHLY
import math

# ASK THE PERSON FOR THE RADIUS OF THE CIRCULAR GARDEN
radius = float(input("Enter the radius of the garden: "))

# CALCULATION FOR THE AREA, CIRCUMFERENCE. SQUARE ROOT, AND THE AREA ROUNDED DOWN AND UP
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
square_root = math.sqrt(area)
rounded_down = math.floor(area)
rounded_up = math.ceil(area)

# DISPLAY THE ANSWER FROM THE CALCULATION
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square root of the area: {square_root:.2f}")
print(f"Area rounded down: {rounded_down} square meters")
print(f"Area rounded up: {rounded_up} square meters")
