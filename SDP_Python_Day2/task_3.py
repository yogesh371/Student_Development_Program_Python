# WAP to cal fibbonacci series 0 1 1 2 3 5 8 13

n = int(input("Enter the number for fibbonacci: "))
num1 = 0
num2 = 1
print(num1)
print(num2)
i = 0
for i in range(2,n):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)