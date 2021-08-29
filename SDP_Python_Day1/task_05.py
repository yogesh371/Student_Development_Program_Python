# Write a program to calculate gross sal from basic sa(HRA=30% , TA = 40%, DA=20%)

Basic_salary = float(input("Enter the basic salary: "))

HRA = Basic_salary * 30/100
TA = Basic_salary * 40/100
DA = Basic_salary * 20/100

Gross_salary = Basic_salary + HRA + TA + DA  

print("House range of 30 % of basic salary:", HRA)
print("Travelling Allowance of 40% of basic salary:", TA)
print("Daily Allowance of 20% of basic salary:", DA)
print("Gross salary from basic salary:", Gross_salary)