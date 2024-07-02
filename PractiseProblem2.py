# 1.	While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.
quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))

if quantity > 1000:
    discount = 0.10 * price_per_item
else:
    discount = 0

total_expenses = quantity * (price_per_item - discount)
print(f"Total expenses: {total_expenses:.2f}")


# 2.	In a company an employee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary. If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the employee's salary is input through the keyboard write a program to find his gross salary.
basic_salary = float(input("Enter the basic salary: "))

if basic_salary < 1500:
    HRA = 0.10 * basic_salary
    DA = 0.90 * basic_salary
else:
    HRA = 500
    DA = 0.98 * basic_salary

gross_salary = basic_salary + HRA + DA
print(f"Gross salary: {gross_salary:.2f}")


# 3.	A company insures its drivers in the following cases: 
# •	If the driver is married. 
# •	If the driver is unmarried, male & above 30 years of age. 
# •	If the driver is unmarried, female & above 25 years of age.
marital_status = input("Is the driver married? (yes/no): ").lower()
age = int(input("Enter the driver's age: "))

if marital_status == "yes" or (not marital_status and (age > 30 or (age > 25 and input("Is the driver female? (yes/no): ").lower() == "yes"))):
    print("Driver is insured.")
else:
    print("Driver is not insured.")



# 4.	Rewrite the following code snippet in 1 line: 
# x = 3 
# y = 3.0 
# if x == y : 
# print('x and y are equal') 
# else : 
# print('x and y are not equal')
x, y = 3, 3.0
print("x and y are equal" if x == y else "x and y are not equal")


# 5.	If a = 10, b = 12, c = 0, find the values of the following expressions: 
# •	a != 6 and b > 5 
# •	a == 9 or b < 3 
# •	not ( a < 10 ) 
# •	not ( a > 5 and c ) 5 and c != 8 or !c
a, b, c = 10, 12, 0
print(a != 6 and b > 5)
print(a == 9 or b < 3)
print(not (a < 10))
print(not (a > 5 and c) and c != 8 or not c)


# 6.	Write a program that prints numbers from 1 to 10 using an infinite loop. All numbers should get printed in the same line.
num = 1
while True:
    print(num, end=" ")
    num += 1
    if num > 10:
        break


# 7.	Write a program to print first 25 odd numbers using range( ).
for num in range(1, 51, 2):
    print(num, end=" ")

# 8.	A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.
original_number = int(input("Enter a five-digit number: "))
reversed_number = int(str(original_number)[::-1])

if original_number == reversed_number:
    print("The original and reversed numbers are equal.")
else:
    print("The original and reversed numbers are not equal.")


# 9.	Write a Python program to print the Fibonacci Series.
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 10.	Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. For example, 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3).
for num in range(1, 501):
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    if sum_of_cubes == num:
        print(num, end=" ")


# 11.	 Evaluate the following expressions: 
# (a) 2 ** 6 // 8 % 2  Ans:-0
# (b) 9 ** 2 // 5 -3   Ans:-13
# (c) 10 + 6 -2 % 3 + 7 -2  Ans:-19
# (d) 5 % 10 + 10 -23 * 4 // 3  Ans:- -15
# (e) 5 + 5 // 5 -5 * 5 ** 5 % 5  Ans:- 6
# (f) 7 % 7 + 7 // 7 -7 * 7  Ans:- -48
# (g) 3 & 5<<2//5**2+10^5   Ans:-4
