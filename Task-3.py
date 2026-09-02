#Task1
name = input("Enter your name: ")
print(name.upper())

#Task 2
sentence = input("Enter the sentence: ")
print(sentence.lower())

#Task 3
sentence = input("Enter the sentence: ")
print(sentence.capitalize())

#Task 4
name =  input("Enter your name: ")
age = int(input("Enter your age: "))
print("I am {}. I am {} years old.".format(name, age))

#Task 5
word = input("Enter the word: ")
print(word.index("o"))

#Task 6
string = input("Enter the string: ")
substring = input("Enter the substring: ")
print(string.find(substring))

#Task 7
word = input("Enter the word: ")
print(word.endswith("ing"))

#Task 8
text = "Name\tAge\tCity"

print("Before expandtabs():")
print(text)

print("\nAfter expandtabs():")
print(text.expandtabs())

#Task 9
text = input("Enter the text: ")

encoded_text = text.encode("utf-8")
print(encoded_text)

#Task 10
text = input("Enter a string: ")

if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

#Task 11
text = input("Enter a string: ")

if text.isnumeric():
    print("The string is numeric.")
else:
    print("The string is not numeric.")

#Task 12
text = input("Enter a string: ")

if text.isalnum():
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")

#Task 13
text = input("Enter a string: ")

if text.isascii():
    print("The string contains only ASCII characters.")
else:
    print("The string contains non-ASCII characters.")

#Task 14
text = input("Enter a string: ")

if text.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string does not contain only alphabets.")
