#Task1
number = int(input("Enter the number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("zero")

#Task2
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Task3
number = int(input("Enter the number: "))

if number % 3 ==0 and number % 5 ==0:
    print("The given number is divisible by 3 and 5")
else:
    print("The given number is not divisible by 3 and 5")

#Task4
units_consumed = int(input("Enter the units consumed: "))
bill_amount = 0

if units_consumed <= 100:
    bill_amount += 100 * 2
elif units_consumed <= 200:
    bill_amount = (100 * 2) + (units_consumed - 100) * 3
elif units_consumed <= 300:
    bill_amount = (100 * 2) + (units_consumed - 100) * 3 + (units_consumed - 100) * 5
else :
    bill_amount = (100 * 2) + (units_consumed - 100) * 3 + (units_consumed - 100) * 5 + units_consumed * 7

print("Total bill amount: ", bill_amount)

#Task5
number = int(input("Enter the number: "))

for i in range(1,21):
    print(number, " x ", i, " = ", (number*i))

#Task6
number = int(input("Enter the number: "))

if number <= 1:
    print("Not a prime number")
else:
    flag = 0
    for i in range(2, number):
        if number % i == 0:
            flag = 1
            break
    if flag == 0:
        print("Prime number")
    else:
        print("Not a prime number")

#Task7
number = int(input("Enter the number of rows: "))

for i in range(1, number+1):
    for j in range(i):
        print("*", end = "")
    print()

#Task8
number = int(input("Enter the number of rows: "))

for i in range(1, number+1):
    for j in range(number-i):
        print(" ", end = "")
    for k in range(2 * i - 1):
        print("*", end = "")
    print()
            
#Task9
number = int(input("Enter the number: "))

for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()

#Task10
year = int(input("Enter the year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
    

#Task11
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

max_num = 0
min_num = 0

if num1 >= num2 and num1 >= num3:
    max_num = num1

    if num2 <= num3:
        min_num = num2
    else:
        min_num = num3

elif num2 >= num1 and num2 >= num3:
    max_num = num2

    if num1 <= num3:
        min_num = num1
    else:
        min_num = num3

else:
    max_num = num3

    if num1 <= num2:
        min_num = num1
    else:
        min_num = num2

print("Maximum number:", max_num)
print("Minimum number:", min_num)

#Task12
year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
