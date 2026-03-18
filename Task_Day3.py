# 1.Print numbers from 1 to 50 using for loop
for i in range(1,51):
    print(i)

# 2. Print even numbers from 1 to 100
for i in range(1,101):
   if i % 2 ==0:
    print(i)

# 3.Print odd numbers from 1 to 100
for i in range(1,101):
    if i % 2 !=0:
     print(i)

# 4.Print multiplication table of 7
for i in range(1,11):
  print(7*i)


# 5.Find sum of numbers from 1 to 100
sum = 0
for i in range(1, 101):
    sum += i
print(sum)


# 6.Print numbers in reverse from 50 to 1
for i in range(50,  0, -1):
    print(i)


# 7.Count how many numbers are divisible by 3 (1–100)
a = 0
for i in range(1,101):
    if i % 3 == 0:
        a += 1
print(a)


# 8.Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i**2)

# 9.Print cube of first 10 numbers
for i in range(1, 11):
    print(i**3)

# Take input n, print numbers from 1 to n
a = int(input("Enter No: "))
for i in range(1, a+1):
  print(i)

########### While Loop ############

# 11.Print numbers from 1 to 20 using while
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1


# 12.Find factorial of a number using while
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# 13.Reverse a number using while
a = int(input("Enter number: "))
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a //= 10
print(rev)


# 14.Count digits in a number
n = int(input("Enter a Nu: "))
count = 0
while n != 0:
    n //= 10
    count += 1
print("Nu of digits =", count)


# 15.Keep asking input until user enters "stop"
while True:
    x = input("Enter something: ")
    if x == "stop":
        break

# 16.Print * pattern:
for i in range(1,5):
    print("*" * i)


# 17.Print Nu(1, 12, 123...) pattern:
for i in range(1,5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
        


# 18.Print multiplication table (1 to 5) using nested loop
for i in range(1,6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

# 19.Print:
# A B C
# A B C
# A B C
for i in range(3):
    for j in ["A", "B", "C"]:
        print(j, end=" ")
    print()

# 20.Print:
# 1 2 3
# 4 5 6
# 7 8 9
a = 1
for i in range(3):
    for j in range(3):
        print(a, end=" ")
        a += 1
    print()

# 21.Count total characters in a string
a = input("Enter : ")
print("Total Characters is: ", len(a))

# 22.Count vowels in a string
vowels={'a','e','i','o','u','A','E','I','O','U'}

text=input("Enter : ")
count = 0
for i in text:
    if i in vowels:
        count+=1
print("Vowel count:",count)


# 23.Count consonants in a string
vowels=['a','e','i','o','u','A','E','I','O','U']

text =input("Enter : ")
count = 0
for i in text:
    if i not in vowels:
        count+=1

print("Consonant Count:",count)


# 24.Reverse a string using loop
a = input("Enter : ")
rev = "".join(reversed(a))
print("Reverse : ", rev)


# 25.Check if string is palindrome
text = input("Enter a string: ")
x = text[::-1]
if text == x:
    print("Palindrome")
else:
    print("Not A Palindrome")

# 26.Print first 5 characters of a string
a = input("Enter : ")
print("First 5 :", a[:5])

# 27.Print last 3 characters
a = input("Enter : ")
print("Last 3:", a[-3:])

# 28.Print string in reverse using slicing
a = input("Enter : ")
print("Reversed word:", a[: : -1])

# 29.Print every 2nd character
a = input("Enter : ")
print("2nd character :", a[::2])

# 30.Remove first and last character from string
a = input("Enter : ")
print("Remove 1st and last char : ", a[1:-1])

# 31.Create a list of 5 numbers and print sum
a = [1, 2, 3, 4, 5]
print("List Sum : ", sum(a))

# 32.Find maximum value in list
a = [8, 4, 11, 6, 3]
print("Max Value : ", max(a))


# 33.Find minimum value in list
a = [5, 8, -3, -7, 1]
print("Min Value : ", min(a))

# 34.Count total elements in list
a = [5, 8, 3, 7, 1]
print("total elements : ", len(a))


# 35.Check if element exists in list
a = [5, 8, 3, 7, 1]
x = int(input("Enter : "))
print(x in a)


# 36.Add 3 elements using append()
a = [10,20]
a.append(30)
a.append(40)
a.append(50)
print(a)

# 37.Insert element at specific index
a = [5, 10, 20, 25]
a.insert(2,15)
print(a)

# 38.Remove element using remove()
a = [5, 10, 20, 25]
a.remove(20)
print(a)

# 39.Reverse list without using .reverse()
a = [5, 10, 15, 20, 25]
revese = a[::-1]
print(revese)

# 40.Sort list without using .sort()
a = [9,3,8,2,5,7,1]
a.sort()
print(a)