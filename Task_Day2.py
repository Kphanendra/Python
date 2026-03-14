# 1. a & b. Bitwise AND operator
a = 10
b = 6
print("AND =",a & b)

#2. x | y.
x = 12
y = 5
print("OR =",x | y)

#3
num = 8
print("NOT =",~num)

#4
a = 15
b = 9
print("XOR =",a ^ b)

#5.Create a variable num = 7.
# Perform left shift by 2 and print the result.
num = 7
print("leftshift =", num << 2)

# 6.Create a variable num = 20.
# Perform right shift by 1 and print the result.
num = 20
print("rightshift =", num >> 1)

#7.Take two numbers from user input and print AND result.
a = int(input("Enter 1st No :"))
b = int(input("Enter 2nd No :"))

print("AND",a&b)


#8.Take two numbers from user input and print XOR result.
x = int(input("Enter your first number :"))
y = int(input("Enter your second number :"))
print("XOR",x^y)


#9.Create a string "hi" and print it 4 times using replication.
string = "hi"
print(string * 4)

#10.Create a string "python" and print it 3 times.
string = "python"
print(string * 3,)

#11.Create two strings "super" and "man" and combine them using + operator.
name1 = "Super"
name2 = "Man"
print(name1 +name2)

# 12.Create three strings "hello", " ", "world" and print "hello world".
word1 = "Hello"
word2 = " "
word3 = "World"
print(word1 + word2 + word3)


# 13.Take a name from user input and print it 5 times.
name = input("Enter your Full Name :")
print("Welcome TO :",name*5)

# 14..Take two strings from user input and concatenate them.
name1 = input("Enter your First Name :")
name2 = input("Enter your Last Name :")
print("Welcome :", name1+name2)

# 15.Take a name from user input and print its data type.
A = input("Enter")
print("Datatype is: ", type(A) )

# 16.Take age from user input and convert it into integer.
age = int(input("Enter Your Age: "))
print(type(age))

# 17.Take two numbers from user input and print their sum.
value1 = int(input("Subject1: "))
value2 = int(input("Subject2: "))
print("Total value = ", value1+value2)

# 18.Take two marks from user input and print their average.
marks1 = int(input("Marks1: "))
marks2 = int(input("Marks2: "))
print("Total Marks = ", (marks1+marks2)/2)

# 19.Take two numbers from user input and print
# 3*a*2 + b - 2.
a = int(input("number1: "))
b = int(input("number2: "))
print(3*a*2 + b - 2)

# 20.Take a number from user input and print its data type before and after type casting.
x = int(input("Enter Any Number: "))
print("Before", type(x))
x = int(x)
print("After", type(x))
print(x)


# 21.Take a number as string input and print the last digit.
num = "123456"
print("Last Digit= ", num[-1])

# 22.Take a number and print the unit digit using % operator.
x = 456
print("Unit Digit= ", x %10 )

# 23.Take a number and remove the last digit using // operator.
y = 98765
print("Last Digit= ", y // 10)

# 24.Take a number and print the second last digit.
z = 123456
print("second last digit= ", (z // 10) % 10)

# 25.Take a 5 digit number and print its last digit.
a = 56789
print("Last digit= ", a % 10)


# 26.Create a program that checks if 10 ≥ 5 and prints a message.
x = 6
if x >= 5:
    print("The value is greter then 5")

# 27.Take a number from user input and check if it is greater than 50.
y = int(input("Enter Value :"))
if y > 50:
    print(y, "is greater then 50")

# 28.Take age from user input and check if age ≥ 18.
age = int(input("Enter your Age :"))
if age >= 18:
    print("your atre over 18")

# 29.Take a number and check if it is greater than 100.
number = int(input("Enter Value :"))
if number > 100:
    print(number,"is greater then 100")

# 30.Take a number and check if number ≥ 0.
number = int(input("Enter Value :"))
if number >= 0:
    print(number,"is positive no: valid")

# 31.Take a number and check if it is even or odd.
x = int(input("Enter your Number :"))
y = x % 2
if y == 0:
    print(x,"is Even Number")
else:
    print(x,"is Odd Number")


# 32.Take marks from user input and check if pass or fail (pass ≥ 35).
marks = int(input("Enter Your Marks :"))
if marks >= 35:
    print("You Are Pass")
else:
    print("You Are Fail")

# 33.Take a number and check if it is positive or negative.
y = int(input("Enter Your Value :"))
if y >= 0:
    print(y, "is Positive No")
else:
    print(y, "is Nagative No")


# 34.Take a number and check if it is greater than 10 or not.
z = int(input("Enter Your Value :"))
if z >= 10:
    print(z, "is greater than 10")
else:
    print(z, "is less than 10")


# 35.
Age = int(input("Enter Your Age: "))
Height = int(input("Enter Your Height: "))
Weight = int(input("Enter Your Weight: "))

if Age >= 18 and Height >=160 and Weight >=60:
    print("You Are Selected")
else:
    print("You Are Rejected")


# 36.
Marks = int(input("Enter Your Marks: "))
Age = int(input("Enter Your Age: "))

if Marks >= 60:
    if age >= 17:
        print("You Are Eligible for Admission ")
    else:
        print("You Are Not Eligible for Admission below Age")
else:
    print("You Are Not Eligible for Admission below Marks")


# 37.
Age = int(input("Enter Your Age: "))
Height = int(input("Enter Your Height: "))
Weight = int(input("Enter Your Weight: "))

if Age >= 16 and Height >=150 and Weight >=50:
    print("You Are Selected")
else:
    print("You Are Rejected")


# 38.Take a number (1-7) and print day name using match.
Day = int(input("Enter Your Week Number: "))
match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Number")



# 39.Take a number (1-3) and print:1 → Red, 2 → Blue, 3 → Green
Colour = int(input("Enter Your Number(1-3): "))
match Colour:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")


# 40. Take a number (1-4) and print:1 → Apple, 2 → Mango, 3 → Orange, 4 → Banana
Fruit = int(input("Enter Your Number(1-4): "))
match Fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")