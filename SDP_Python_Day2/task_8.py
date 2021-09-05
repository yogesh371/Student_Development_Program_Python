# Enter Five Ingere Number And Find Maximum Number (using simple if)


n1 = int(input("Enter First Numbers: "))
n2 = int(input("Enter Second Numbers: "))
n3 = int(input("Enter Third Numbers: "))
n4 = int(input("Enter Fourth Numbers: "))
n5 = int(input("Enter Fifth Numbers: "))

if (n1>n2) and (n1>n2) and (n1>n3) and (n1>n4) and (n1>n5):
    print("The Maximum Number is: ", n1)

elif (n2>n3) and (n2>n4) and (n2>n5):
    print("The Maximum Number is: ", n2)

elif (n3>n4) and (n3>n5):
    print("The Maximum Number is: ", n3)

elif (n4>n5):
    print("The Maximum Number is: ", n4)

else:
    print("The Maximum Number is: ", n5)

