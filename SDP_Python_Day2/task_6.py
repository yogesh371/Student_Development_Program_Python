# WAP to find armstrong number 1234=1^4+2^4+3^4+4^4 = 

n = int(input("Enter The Number: "))
num = n
num_string = str(n)
base = len(num_string)
arm =  0
rem = 0

while(num>0):
    rem = num % 10
    arm = arm + rem ** base
    num = num // 10

if(arm==n):
    print(n, "is Armstrong Number")
else:
    print(n, "is not Armstrong Number")