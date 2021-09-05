# WAP To cal factorial of any number 5!=120
n = int(input("Enter the number: "))

fact = 1

for i in range (1,n+1):
    fact = fact * i

print("The factorial of a given number is: ",fact)