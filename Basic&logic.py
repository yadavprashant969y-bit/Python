# (1). Take two numbers and print their sum, difference, and product.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")


## (2). Input a number and check if it is positive, negative, or zero.


number = float(input("Enter a number: "))   
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    
    
    
## (3).Input a number and print whether it’s even or odd.

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("{num} is even.")
else:
    print("{num} is odd.") 



## (4).Input marks of 5 subjects; print total, average, and percentage.

marks = []
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100  

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Percentage: {percentage}%")



##(5).Take a temperature in Celsius and convert to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")   



##(6). Swap two variables without using a third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swap: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swap: a = {a}, b = {b}")



##(7).Input a three-digit number and print its reverse.

num = int(input("Enter a three-digit number: "))
reversed_num = int(str(num)[::-1])
print(f"Original number: {num}")
print(f"Reversed number: {reversed_num}")



##(8).Input age; check if eligible for voting.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
    print(f"You need to wait {18 - age} more years to be eligible.")



##(9). Input a number; print multiplication table (1–10).

num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")



##(10). Input three numbers; print the largest.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")
