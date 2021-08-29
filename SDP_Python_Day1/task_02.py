# Write a program to calculate simple interest

p = int(input("Enter the principle amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate: "))

simple_interest = p * r * t / 100

print("The simple interest is: ",simple_interest)