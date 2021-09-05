# WAP to find palindrome number

n = int(input("Enter the Number: "))
num = n
rev = 0
while n>0:
    rev = ((rev*10) + (n % 10))
    n = n//10

if rev==num:
    print("The Entered Number is palindrome")
else:
    print("The Entered Number is not palindrome")
