#Fibonacci series and factorial using Function
def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b

def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


n = int(input("Enter the number: "))
print("Fibonacci Series: ", end=" ")
fib(n)
print("\nFactorial: ", fact(n))

#Find the length of a string
string = input("Enter the string: ")
print("Length of the string: ", len(string))

#Find the maximum value of the number
numbers = [11,12,22,34,54,14]
print("Maximum Number: ", max(numbers))

#Find the minimum value of the number
numbers = [11,12,22,34,54,14]
print("Minimum Number: ", min(numbers))

#Find the sum of the number
numbers = [11,12,22,34,54,14]
print("Sum of the number: ", sum(numbers))

#Factorial using recursion function
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

n = int(input("Enter the number: "))
print("Factorial of the given number: ", fact(n))

#Write a function student_details(name, roll, dept) that prints the details using positional arguments

def student_details(name, roll, dept):
    print("Name: ",name,"\n","Roll No: ",roll,"\n","Dept: ",dept)

student_details("Vigneshwaran M", 62, "CSE")

#Write a function calculate_total(marks1, marks2, marks3) to calculate the total marks of a student using positional
def calculate_total(marks1, marks2, marks3):
    return marks1+marks2+marks3

print("Total Marks: ", calculate_total(92,95,94))

#Write a function rectangle_area(length, width) that calculates the area of a rectangle using positional argument
def rectangle_area(length, width):
    return length * width

length = 5
width = 6
print("Area of a rectangle: ", rectangle_area(length, width))

#Write a function greet_user(name, message="Good Morning") that prints a greeting using default argument
def greet_user(name, message="Good Morning"):
    print(message,name,"!")

name =input("Enter the name: ")
greet_user(name, message="Good Morning")

#Write a function add_numbers(*args) that returns the sum of any number of values
def add_numbers(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print("Sum of numbers: ",add_numbers(1,2,3,4,5,6,7))

#Write a function multiply_all(*args) that multiplies any number of values
def multiply_all(*args):
    multiply = 1
    for n in args:
        multiply *= n
    return multiply

print("Multiplication of numbers: ",multiply_all(1,2,3,4,5))

#Write a function to add two numbers
def add_two_numbers(num1, num2):
    return num1+num2

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
print("Addition of two numbers: ", add_two_numbers(num1, num2))

#Write a function to find the square of a number
def square_number(num):
    return num*num

num = int(input("Enter the number:"))
print("Square of a number: ", square_number(num))

#Write a function to check whether a number is even or odd
def odd_even(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter the number:"))
odd_even(num)

#Write a function to find the maximum of two numbers
def max_of_two(num1, num2):
    if num1 > num2:
        print(num1," is greater")
    else:
        print(num2, " is greater")

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
max_of_two(num1, num2)

