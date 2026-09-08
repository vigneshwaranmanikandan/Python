#Reverse a string without using slicing
s = input("Enter the string: ")
rev_str = ""
for i in range(len(s)-1, -1, -1):
    rev_str += s[i]
print(rev_str)

#Check if a string is a palindrome
s = input("Enter the string: ")
rev_str = ''.join(reversed(s))
if s == rev_str:
    print("Palindrome")
else:
    print("Not Palindrome")

#Count how many times a particular word appears in a sentence
sentence = input("Enter the sentence: ")
word = input("Enter the word: ")
cnt=0
for text in sentence.split():
    if text == word:
        cnt+=1
print(word, " appears ", cnt, " times")

#Find the longest word in a sentence
s = input("Enter the string: ")
longest_str = ""
for word in s.split():
    if(len(word) > len(longest_str)):
        longest_str = word
print(longest_str)

#Replace spaces in a string with hyphens
s = input("Enter the string: ")
s = s.replace(" ", "-")
print(s)

#Count digits, letters, and special characters in a string
s = input("Enter the string: ")
digits = 0
letters = 0
s_char = 0
for char in s:
    if char.isdigit():
        digits+=1
    elif char.isalpha():
        letters+=1
    else:
        s_char+=1
        
print("Digits:", digits)
print("Letters:", letters)
print("Special characters:", s_char)

string = input("Enter the string: ").lower()
vowels = 0
consonants = 0
for c in string:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        vowels+=1
    elif c == ' ':
        continue
    else:
        consonants += 1
print("Vowels: ", vowels)
print("Consonants: ", consonants)
