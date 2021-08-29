# WAP to enter height of user in feets and convert it into inches and centimeter(1 feet = 12 inch, 1 inch = 2.54cm)

height = float(input("Enter your height in feets: "))

in_Inches = height * 12 

in_Centimeters = 2.54 * in_Inches

print("Your height in inches is:", in_Inches)
print("Your height in centimeters is:", in_Centimeters)