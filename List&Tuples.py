
# ### 1. Input 10 numbers into a list and print the second largest

print("=" * 50)
print("1. Second Largest Number")
print("=" * 50)
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

sorted_numbers = sorted(set(numbers), reverse=True)
if len(sorted_numbers) >= 2:
    print(f"Second largest: {sorted_numbers[1]}")
else:
    print("Not enough unique numbers")
    
    
    

### 2. Remove duplicates from a list without using set()

print("\n" + "=" * 50)
print("2. Remove Duplicates (without set())")
print("=" * 50)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
print(f"Original list: {list_with_duplicates}")

unique_list = []
for item in list_with_duplicates:
    if item not in unique_list:
        unique_list.append(item)
print(f"List without duplicates: {unique_list}")





### 3. Count how many times each item appears in a list
print("\n" + "=" * 50)
print("3. Count Item Occurrences")
print("=" * 50)
items_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
print(f"List: {items_list}")

count_dict = {}
for item in items_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Item counts:")
for item, count in count_dict.items():
    print(f"  {item} appears {count} time(s)")
    
    
    

### 4. Merge two lists and sort them
print("\n" + "=" * 50)
print("4. Merge and Sort Two Lists")
print("=" * 50)
list1 = [5, 2, 8, 1]
list2 = [9, 3, 6, 4]
print(f"List 1: {list1}")
print(f"List 2: {list2}")

merged_list = list1 + list2
merged_list.sort()
print(f"Merged and sorted: {merged_list}")




### 5. Convert a list to tuple and tuple back to list
print("\n" + "=" * 50)
print("5. Convert List to Tuple and Back")
print("=" * 50)
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

my_tuple = tuple(my_list)
print(f"Converted to tuple: {my_tuple}")

back_to_list = list(my_tuple)
print(f"Converted back to list: {back_to_list}")



### 6. Find the sum of all elements in a list without using sum()
print("\n" + "=" * 50)
print("6. Sum Without Using sum()")
print("=" * 50)
numbers_to_sum = [10, 20, 30, 40, 50]
print(f"List: {numbers_to_sum}")

total = 0
for num in numbers_to_sum:
    total += num
print(f"Sum: {total}")



###7. Reverse a list using slicing
print("\n" + "=" * 50)
print("7. Reverse List Using Slicing")
print("=" * 50)
list_to_reverse = [1, 2, 3, 4, 5]
print(f"Original list: {list_to_reverse}")

reversed_list = list_to_reverse[::-1]
print(f"Reversed list: {reversed_list}")



### 8. Given a tuple of numbers, print all numbers greater than 50
print("\n" + "=" * 50)
print("8. Numbers Greater Than 50 in Tuple")
print("=" * 50)
number_tuple = (10, 25, 60, 45, 75, 30, 90, 15)
print(f"Tuple: {number_tuple}")

greater_than_50 = [num for num in number_tuple if num > 50]
print(f"Numbers greater than 50: {greater_than_50}")




### 9. Find the index of a value in a tuple (handle value not present)
print("\n" + "=" * 50)
print("9. Find Index in Tuple (with error handling)")
print("=" * 50)
search_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(f"Tuple: {search_tuple}")


search_value = 'cherry'
try:
    index = search_tuple.index(search_value)
    print(f"Index of '{search_value}': {index}")
except ValueError:
    print(f"'{search_value}' not found in tuple")


search_value2 = 'mango'
index_found = -1
for i, item in enumerate(search_tuple):
    if item == search_value2:
        index_found = i
        break

if index_found != -1:
    print(f"Index of '{search_value2}': {index_found}")
else:
    print(f"'{search_value2}' not found in tuple")
    
    
    
    

### 10. Multiply all elements of a list
print("\n" + "=" * 50)
print("10. Multiply All Elements")
print("=" * 50)
numbers_to_multiply = [2, 3, 4, 5]
print(f"List: {numbers_to_multiply}")

product = 1
for num in numbers_to_multiply:
    product *= num
print(f"Product of all elements: {product}")

print("\n" + "=" * 50)
print("All operations completed!")
print("=" * 50)