#Find the largest and smallest number in a list
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


#Remove duplicates from a list
numbers = [1,2,3,1,3,2,4]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

#Calculate the sum and average of numbers in a list
numbers = [1,2,3,4,5]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

l = [3,4,1,5,2]

#Sort a list in ascending and descending order
l.sort()
print("Ascending: ",l)

l.sort(reverse=True)
print("Descending: ",l)

#Create a list of cubes for numbers 1–10
result = []

for i in range(1,11):
    result.append(i ** 3)

print(result)

#Find the second largest number in a list
l= [12,13,53,14,86]
first = l[0]
second = l[0]

for i in range(1, len(l)):
    if l[i] > first:
        second = first
        first = l[i]
    elif l[i] > second and l[i] < first:
        second = l[i]

print("First Largest: ", first)
print("Second Largest: ", second)
        
#Merge two lists into one

l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)

print(l1)

#Access the 2nd and 4th elements of a tuple
t = (10,20,30,40,50)

print("2nd: ", t[1], " 4th: ",t[3] )

#Check if an element exists in a tuple
t = (1,2,3,4,5)
n = int(input("Enter the element: "))
if n in t:
    print("exists")
else:
    print("not exists")

#Convert a tuple into a list and back into a tuple
t1 = (1,2,3,4,5)
l1 = list(t1)
print("List: ", l1)
t2 = tuple(l1)
print("Tuple: ", t2)

#Find the length, maximum, and minimum in a tuple
t = (1,2,3,4,5)
print("Length: ", len(t))
print("Maximum: ", max(t))
print("Minimum: ", min(t))

#Concatenate two tuples
t1 = (1,2,3)
t2 = (4,5,6)
result = t1 + t2
print(result)
