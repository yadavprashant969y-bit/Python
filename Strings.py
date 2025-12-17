##(1). Input a string and count vowels, consonants, digits, and spaces.

string = input("Enter a string: ")

vowels = consonants = digits = spaces = 0

for char in string:
    if char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    elif char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Spaces: {spaces}")

##(2).Check if a given string is a palindrome.

s = input("Enter a string: ")
s = s.replace(" ", "").lower()

if s == s[::-1]:
    print("Palindrome") 
else:
    print("Not a palindrome")



##(3). Replace all spaces in a sentence with -.

sentence = input("Enter a sentence: ")
modified_sentence = sentence.replace(" ", "-")
print("Modified sentence:", modified_sentence)    



##(4). Print characters at even index positions.

string = input("Enter a string: ")
print("Characters at even index positions:", string[::3])




##(5). Input a sentence and print each word on a new line.

sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    print(word)



##(6). Count occurrences of a specific character in a string.

string = input("Enter a string: ")
char = input("Enter a character to count: ")
count = 0

for c in string:
    if c == char:
        count += 1

print(f"The character '{char}' occurs {count} times in the string.")



##(7).Find the longest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest_word = max(words, key=len)
    print(f"The longest word is: {longest_word}")
else:
    print("No words found")



##(8). Remove duplicate characters from a string.

string = input("Enter a string: ")
unique_chars = ''.join(dict.fromkeys(string))

print(f"String without duplicates: {unique_chars}")



