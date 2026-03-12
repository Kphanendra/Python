# Task-1
print("Hello World Welcome Python")
print("Laptop, Mouse, Keyboard", sep=" | ")

# Task-2 (Variables)
name = "Ravi"
age = 22
city = "Chennai" #Print in one line separated by -

print(name,age,city, sep="-")

# Task-3 (Multiple Assignment)
name,age,student= "Meena",20,True
print(name,age,student)


# Task-4 (Indexing)
word = "PYTHON"

print("First:", word[0], "Middle:", word[2], "Last:", word[-1] )

# Task-5 (Arithmetic Operators)
print("25+10 =", 25+10)    # 35, Adition Operator
print("50-20 =", 50-20)    # 30, Subtraction Operator
print("8*5 =",8*5)      # 40, Multiplication Operator
print("100/10 =", 100/10)   # 10.0, Division Operator
print("10%3 =", 10%3)     # 1, Modulus Operator
print("2**4 =", 2**4)     # 16, EXPONENTIAL Operator
print("20//3 =", 20//3)    # 6, FLOOR DIVISION Operator


# Task-6 (BODMAS)
print("3 + 2 * 5 ** 2 :", 3 + 2 * 5 ** 2)
''''ans is 53   BODMAS rule applicable'''

# Task-7 (Assignment Operator)
num=50
num+=25
print("final value =", num)

num=100
num/=10
print("final value =", num)

# Task-8 (Comparison Operators)
print("10 > 5 :", 10 > 5)  #True 
print("20 < 15 :", 20 < 15) #False
print("5 == 5 :", 5 == 5)  #True 
print("10 != 8 :", 10 != 8) #True
print("7 >= 7 :", 7 >= 7)  #True
print("6 <= 2 :", 6 <= 2)  #False


# Task-9 (String Comparison)
a = "apple"
b = "Apple"

print("a == b :", a == b)   #False
'''small"a", capital "A"  has different ascii values '''


# Task-10 (Logical)
print("10 > 5 and 5 == 5 :", 10 > 5 and 5 == 5)    #True
print("5 > 10 or 10 == 10 :", 5 > 10 or 10 == 10)   #True
print("not(5 > 2) :", not(5 > 2))   #False


# Task-11 (Membership)
numbers=[10,20,30,40,50]
print("20 in numbers=", 20 in numbers)    #True
print("60 in numbers=", 60 in numbers)    #False
print("30 in numbers=", 30 not in numbers)    #False

# Task-12 (Swap)
a=10
b=20
a,b=b,a
print("a=",a)
print("b=",b)

# Task-13 (Bitwise XOR)
a=6
b=3
print("a^b=", a^b)

