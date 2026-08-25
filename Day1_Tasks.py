#Task1
sub1 = int(input("Enter mark of subject 1: "))
sub2 = int(input("Enter mark of subject 2: "))
sub3 = int(input("Enter mark of subject 3: "))

if sub1 >= 50 and sub2 >= 50 and sub3 >= 50:
    print("Student is eligible for admission")
else:
    print("Student is not eligible for admission")

#Task2
salary = int(input("Enter salary: "))
experience = int(input("Enter the years of experience: "))
performance_rating = input("Enter the performance rating(A/B/C): ").upper()

if experience > 3 and performance_rating == 'A':
    bonus = salary * 0.3
    print("Bonus: ",bonus)
elif experience > 3 and performance_rating == 'B':
    bonus = salary * 0.2
    print("Bonus: ",bonus)
elif experience > 3 and performance_rating == 'C':
    bonus = salary * 0.1
    print("Bonus: ",bonus)
else:
    print("The person is not eligible for bonus")

#Task3
purchase_amount = int(input("Enter the purchase amount: "))
membership_status = input("Enter the membership status(yes/no): ").lower()
festival_offer = input("Is festival offer available(yes/no): ").lower()

if purchase_amount >= 3000 and membership_status == "yes" and festival_offer == "yes":
    offer_amount  = purchase_amount * 0.3
    final_shopping_amount = purchase_amount - offer_amount
    print("Final shopping amount: ", final_shopping_amount)
else:
    print("This shopping is not eligible for offer")

#Task4
username = input("Enter the username: ")
password = input("Enter the password: ")
otp = input("Enter the OTP: ")

if username == "vignesh" and password == "1234" and otp == "987654":
    print("Login successful!")
else:
    print("Login failed")

#Task5
withdrawl_amount = int(input("Enter the amount to withdraw: "))
account_balance = 5000
minimum_balance = 1000

if withdrawl_amount <= account_balance and (account_balance - withdrawl_amount) > minimum_balance and withdrawl_amount % 100 == 0:
    account_balance -= withdrawl_amount
    print("Amount withdrew successfully. Available Balance = ", account_balance)
else:
    print("The amount cannot be withdraw")

#Task6
list1 = [10,20,30]
list2 = [10,20,30]

print(list1 == list2)
print(list1 is list2)

list2 = list1

print(list1 == list2)
print(list1 is list2)

#Task7
sentence = "I LIKE GREEN COLOR"
list = ["BLUE", "GREEN", "RED"]
word = input("Enter the word to search: ").upper()

if word in sentence:
    print("The word present in sentence")
else:
    print("The word is not in sentence")

if word in list:
    print("The word is present in list")
else:
    print("The word is not in list")

#Task8
number = int(input("Enter the number to validate: "))

if number > 0  and number < 100 and ((number % 3 == 0 and number % 5 !=0) or (number % 3 != 0 and number % 5 == 0)):
    print("It is a valid number")
else:
    print("It is not a valid number")
