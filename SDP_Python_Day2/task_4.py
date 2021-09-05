# WAP for LCM, HCF, GCD

print("Enter Two Numbers: ")
n1 = int(input("Enter Number one: "))
n2 = int(input("Enter Number two: "))

a = n1 
b = n2
while b!=0:
    temp = b
    b = a%b
    a = temp

hcf = a
lcm = int((n1*n2)/hcf)

print("\nLCM is ", lcm)
print("HCF is ", hcf)