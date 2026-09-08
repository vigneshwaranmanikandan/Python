#Check if a number is positive, negative, or zero
n = int(input("Enter a number: "))
if(n<0):
    print("Negative")
elif(n>0):
    print("Positive")
else:
    print("Zero")

#Find the largest of three numbers
n1=int(input("Enter the number 1: "))
n2=int(input("Enter the number 2: "))
n3=int(input("Enter the number 3: "))
if (n1>n2) and (n1>n3):
    print("Number 1")
elif (n2>n1) and (n2>n3):
    print("Number 2")
else:
    print("Number 3")

#Print the multiplication table of a given number
n=int(input("Enter the number: "))
for i in range(1,21):
    print(n, " x ", i, " = ", (n*i))

#Check if a year is a leap year
year = int(input("Enter the year: "))
if ((year%4==0) and (year%100!=0)) or (year%400==0):
    print("Leap year")
else:
    print("Not a Leap year")
    

mark = int(input("Enter the mark: "))
if mark >= 40:
    print("Passed")
else:
    print("Failed")

#Keep asking the user for a password until they enter the correct one
password = int(input("Enter the password: "))
while password != 1234:
    password = int(input("Enter the password: "))
print("Login Successful")

#Print the first 10 Fibonacci numbers
a = 0
b = 1
for i in range(10):
    print(a)
    a, b = b, a + b

#Print numbers from 1 to 20, but skip multiples of 3
for i in range(1, 21):
    if i%3==0:
        continue
    print(i," ")
    

#Find the factorial of a number using a loop
n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact*=i

print(fact)

#Count how many even numbers are between 1 and 50
cnt = 0
for i in range(1, 51):
    if i%2 ==0:
        cnt+=1
print(cnt)
