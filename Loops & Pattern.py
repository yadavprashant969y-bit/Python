### 1. Right-angle star pattern

print("=== Right-Angle Star Pattern ===")
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("*" * i)
    
    
    

### 2. Pyramid pattern

print("\n=== Pyramid Pattern ===")
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
    
    

### 3. Sum of digits of a number using a loop

print("\n=== Sum of Digits ===")
num = int(input("Enter a number: "))
temp = num
digit_sum = 0
while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10
print(f"Sum of digits of {num} is: {digit_sum}")




### 4. Find factorial of a number using a loop

print("\n=== Factorial ===")
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")




### 5. Print numbers from 1 to 100 skipping multiples of 3

print("\n=== Numbers 1-100 (skip multiples of 3) ===")
for i in range(1, 101):
    if i % 3 != 0:
        print(i, end=" ")
print()




### 6. Find prime numbers between 1 and 100

print("\n=== Prime Numbers between 1 and 100 ===")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()




### 7. Print Fibonacci series up to n terms

print("\n=== Fibonacci Series ===")
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()




### 8. Count how many digits are in a number (no string conversion)
print("\n=== Count Digits ===")
num = int(input("Enter a number: "))
temp = abs(num)  # Use absolute value to handle negative numbers
count = 0
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
print(f"Number of digits in {num} is: {count}")