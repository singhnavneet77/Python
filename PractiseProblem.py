# 1.	Write a Python program to calculate the electricity bill (accept number of units from user) according to the following criteria:
# Unit	Price
# First 100 units	No charge
# Next 100 units	Rs. 5 per unit
# After 200 units	Rs. 10 per unit
units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill_amount = 0
elif units <= 200:
    bill_amount = (units - 100) * 5
else:
    bill_amount = 100 * 5 + (units - 200) * 10

print(f"Total bill amount: Rs. {bill_amount}")


# 2.	Write a Python program to display the last digit of a number.
number = int(input("Enter a number: "))
last_digit = number % 10
print(f"The last digit of {number} is {last_digit}")


# 3.	Write a Python program to check whether the last digit of a number (entered by the user) is divisible by 6 or not.
number = int(input("Enter a number: "))
last_digit = number % 10
if last_digit % 6 == 0:
    print(f"The last digit ({last_digit}) is divisible by 6.")
else:
    print(f"The last digit ({last_digit}) is not divisible by 6.")

# 4.Check if a Number is Three-Digit:
number = int(input("Enter a number: "))
if 100 <= number <= 999:
    print(f"{number} is a three-digit number.")
else:
    print(f"{number} is not a three-digit number.")



# 5.Triangle Type (Equilateral, Isosceles, or Scalene):
number = int(input("Enter a number: "))
if 100 <= number <= 999:
    print(f"{number} is a three-digit number.")
else:
    print(f"{number} is not a three-digit number.")


side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("It's an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It's an isosceles triangle.")
else:
    print("It's a scalene triangle.")


# 6.Sum of Odd Numbers in a Range:
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_odd = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        sum_odd += num

print(f"Sum of odd numbers from {start} to {end}: {sum_odd}")


# 7.	Write a Python program to find the largest number in a list using a for loop.
numbers = [int(x) for x in input("Enter a list of numbers (separated by spaces): ").split()]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number in the list is: {largest}")


# 8.	Write a Python program to find the average of numbers in a list using a for loop.
numbers = [int(x) for x in input("Enter a list of numbers (separated by spaces): ").split()]
total = sum(numbers)
average = total / len(numbers)

print(f"The average of the numbers in the list is: {average:.2f}")


#9.	Write a Python program to calculate the factorial of a number (entered by the user) using while loop.
number = int(input("Enter a positive integer: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"The factorial of the number is: {factorial}")


#10.	Write a Python program to find the first occurrence of a number in a list using while loop.
numbers = [int(x) for x in input("Enter a list of numbers (separated by spaces): ").split()]
target = int(input("Enter the number to search for: "))
index = 0

while index < len(numbers):
    if numbers[index] == target:
        print(f"{target} found at index {index}.")
        break
    index += 1
else:
    print(f"{target} not found in the list.")
