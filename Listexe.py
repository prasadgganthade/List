#1. Python program to interchange first and last elements in a list

"""
method -1
def swap_list(list):
    size = len(list)

    temp_list = list[0]
    list[0] = list[size - 1]
    list[size - 1]=temp_list
    return list
print(swap_list(list))
"""

# method 2
"""
list = [1,2,3,4]
def swap_list(list):
    list[0],list[-1] = list[-1],list[0]
    return list
print(swap_list(list))
"""
# Python | Ways to find length of list
#list = [10,20,30,40]
#print(len(list))
name = 'How are you'
count = 0
for i in name:
    count = count + 1
print(count)
print(len(name))
# Maximum of two numbers in Python
a = 20
b = 12
if a > b:
    print('Maximum is',a)
else:
    print('Minimum is',b)
maximum = max(a,b)
print(maximum)


# find minimum number
if a <= b:
    print(a)
else:
    print(b)
minimum = min(a,b)
print(minimum)
# to check wheather present or not
#list = [1,3,7,5,9,12]
i = 5
#if i in list:
#    print('Exist')
#else:
#    print('Not exist')
#for i in list:
#    if i == 7:
#        print('Exist')
#Different ways to clear a list in Python
list1 = [1,2,3,4,5]
list1.clear()
print(list1)
# reverseing a list
list2 = [10,20,30,40,50]
list2.reverse()
print(list2)
# by using reversed function
print('Using reversed',tuple(reversed(list2)))
# Python code to count the number of occurrences
num = [8,6,8,10,8,20,8]
count = 0
for i in num:
    if i == 8:
        count = count + 1
print(count)
#Find sum and average of List in Python
l = [15,24,56,89,85]
sum = 0
for i in l:
    sum += i
print(sum)
avg = sum /len(l)
print(avg)
#Multiply all numbers in the list
mul = 1
for i in l:
    mul *= i
print(mul)

def multiply(l):
    result = 1
    for i in l:
        result = result * i
    return result
print(multiply(l))
#Python program to find smallest number in a list
list1 = [10,20,4]
list1.sort()
print(list1[0])
# decending order
list2 = [25,2,56,1]
list2.sort(reverse=True)
print(list2[-1])
print(min(list1))
# for largest number
print(max(list1))
print(list2[0])
#Python program to find second largest number in a list
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
list2 = list(set(list1))
print(list2)
list2.sort()
print(list2)
print(list2[-2])
# now using for loop
def find_largest_number(a):
    second_largest = 0
    largest = min(a)

    for i in range(len(a)):
        if a[i] >largest:
            second_largest = largest
            largest = a[i]
        else:
            second_largest = max(second_largest,a[i])

    return second_largest
print(find_largest_number(list2))
#Python program to print even numbers in a list
list1 = [10, 21, 4, 45, 66, 93]
# using for loop
for i in list1:
    if i % 2 == 0:
        print(i, end=" ")
# using while loop
print()
num = 0
while(num < len(list1)):
    if list1[num] % 2 ==0:
        print(list1[num],end=" ")

    num += 1
print()
#Python program to print odd numbers in a List
list1 = [10, 21, 4, 45, 66, 93]
# using for loop
for i in list1:
    if i % 2 != 0:
        print(i, end=" ")
# using while loop
print()
num = 0
while(num < len(list1)):
    if list1[num] % 2 != 0:
        print(list1[num],end=" ")

    num += 1
print()
# Python program to print all even numbers in a range
for i in range(4,12,2):
    print(i, end=" ")
print()
for i in range(0,101):
    if i % 2 == 0:
        print(i, end=' ')
print()
## Python program to print all odd numbers in a range
for i in range(3,12,2):
    print(i, end=" ")
print()
for i in range(0,101):
    if i % 2 != 0:
        print(i, end=' ')
print()
# Python program to count Even and Odd numbers in a List

"""
for i in list1:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count +1
print('Even count in list is',even_count)
print('Odd count in list is',odd_count)
"""

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

even_count, odd_count = 0, 0
num = 0

# using while loop
while (num < len(list1)):

    # checking condition
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # increment num
    num += 1
print()
#Python program to print positive numbers in a list
nums = [34, 1, 0, -23, 12, -88]
# using for loop
for i in nums:
   if i > 0:
      print(i, end = " ")
print()
# using while loop
a =0
while(a < len(nums)):
    if nums[a] > 0:
        print(nums[a], end=" ")
    a+=1


