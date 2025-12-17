###1. UNION, INTERSECTION, AND DIFFERENCE OF TWO SETS

print("=" * 60)
print("1. Set Operations: Union, Intersection, Difference")
print("=" * 60)

set1 = set(input("Enter first set (space-separated): ").split())
set2 = set(input("Enter second set (space-separated): ").split())

print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference (Set1 - Set2): {set1.difference(set2)}")
print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")


### 2. DICTIONARY OF STUDENT MARKS AND FIND TOPPER

print("\n" + "=" * 60)
print("2. Student Marks - Find Topper")
print("=" * 60)

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 88
}

print("\nStudent Marks:")
for name, marks in students.items():
    print(f"  {name}: {marks}")

topper = max(students, key=students.get)
max_marks = students[topper]
print(f"\nTopper: {topper} with {max_marks} marks")




### 3. WORD FREQUENCY COUNTER FROM PARAGRAPH 

print("\n" + "=" * 60)
print("3. Word Frequency Counter")
print("=" * 60)

paragraph = input("Enter a paragraph: ").lower()
words = paragraph.split()

word_freq = {}
for word in words:
    
    word = word.strip('.,!?;:')
    if word:  # 
        word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}")




### 4. REMOVE KEY-VALUE PAIR FROM DICTIONARY

print("\n" + "=" * 60)
print("4. Remove Key-Value Pair from Dictionary")
print("=" * 60)

sample_dict = {"name": "John", "age": 25, "city": "NYC", "country": "USA"}
print(f"Original Dictionary: {sample_dict}")

key_to_remove = input("Enter key to remove: ")

if key_to_remove in sample_dict:
    removed_value = sample_dict.pop(key_to_remove)
    print(f"Removed '{key_to_remove}': {removed_value}")
else:
    print(f"Key '{key_to_remove}' not found!")

print(f"Updated Dictionary: {sample_dict}")




###  5. CONVERT TWO LISTS INTO DICTIONARY 

print("\n" + "=" * 60)
print("5. Convert Two Lists into Dictionary")
print("=" * 60)

keys = input("Enter keys (space-separated): ").split()
values = input("Enter values (space-separated): ").split()


combined_dict = dict(zip(keys, values))
print(f"\nKeys: {keys}")
print(f"Values: {values}")
print(f"Combined Dictionary: {combined_dict}")




###  6. REVERSE DICTIONARY (SWAP KEYS AND VALUES) 

print("\n" + "=" * 60)
print("6. Reverse Dictionary (Swap Keys & Values)")
print("=" * 60)

dict_to_reverse = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Original Dictionary: {dict_to_reverse}")

reversed_dict = {v: k for k, v in dict_to_reverse.items()}
print(f"Reversed Dictionary: {reversed_dict}")




### 7. FIND COMMON VALUES BETWEEN TWO DICTIONARIES 

print("\n" + "=" * 60)
print("7. Find Common Values Between Two Dictionaries")
print("=" * 60)

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}
dict2 = {"x": 20, "y": 30, "z": 50, "w": 40}

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")

values1 = set(dict1.values())
values2 = set(dict2.values())
common_values = values1.intersection(values2)

print(f"Values in Dict1: {values1}")
print(f"Values in Dict2: {values2}")
print(f"Common Values: {common_values}")




### 8. COUNT UNIQUE VALUES ACROSS DICTIONARY ITEMS 

print("\n" + "=" * 60)
print("8. Count Unique Values Across Dictionary Items")
print("=" * 60)

data_dict = {"item1": "apple", "item2": "banana", "item3": "apple", 
             "item4": "cherry", "item5": "banana", "item6": "date"}

print(f"Dictionary: {data_dict}")

unique_values = set(data_dict.values())
print(f"Unique Values: {unique_values}")
print(f"Total Unique Values: {len(unique_values)}")

value_count = {}
for value in data_dict.values():
    value_count[value] = value_count.get(value, 0) + 1

print("Value Frequency:")
for value, count in value_count.items():
    print(f"  '{value}': {count}")
    
    


### 9. PRINT ALL UNIQUE ELEMENTS FROM A LIST USING SET 

print("\n" + "=" * 60)
print("9. Unique Elements from List Using Set")
print("=" * 60)

input_list = list(map(int, input("Enter numbers (space-separated): ").split()))
print(f"Original List: {input_list}")

unique_elements = set(input_list)
print(f"Unique Elements: {unique_elements}")
print(f"Total Unique Elements: {len(unique_elements)}")
print(f"Duplicates Removed: {len(input_list) - len(unique_elements)} removed")