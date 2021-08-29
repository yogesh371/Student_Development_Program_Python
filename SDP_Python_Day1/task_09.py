# WAP to reverse three numbers 123 = 321

num = 123

print("The Number Before reverse:", num)
rev = 0
while num>0:
    rev = ((rev*10) + (num % 10))
    num = num//10

print("The number After reversing:", rev)