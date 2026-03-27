
# * Task 1: User Info Manager (Functions + Dictionary) *********
def create_user(name, age, role):
  
    return {
        "name": name.title(),
        "age": age,
        "role": role.title()
    }

# Store multiple users in a list
users_list = []

users_list.append(create_user("phani", 25, "engineer"))
users_list.append(create_user("kumar", 30, "developer"))
users_list.append(create_user("vijay", 28, "tester"))

# Print all users
print("********* User Directory *********")
for user in users_list:
    print(f"Name: {user['name']} || Age: {user['age']} || Role: {user['role']}")



# =================================================
# * Task 2: Dynamic Calculator (*args) **************

def calculate_total():
    numbers = []
    print("Enter numbers (type 'done' to Calculate):")

    while True:
        data = input("input = ")
        if data == 'done':
            break
        try:
            numbers.append(float(data))
        except ValueError:
            print("Enter Numbers Only.")

    if numbers:
        total = sum(numbers)
        print("_" *25)
        print(f"Sum of inputs : {total}")
        print(f"Average of inputs : {total / len(numbers):.2f}")
        print("_" *25)
    else:
        print("No Numbers Entered.")

calculate_total()



# =================================================
# * Task 3: Keyword Config System (**kwargs) *******
def show_config(**settings):
    print("\n***Current Configuration***")
    print("_" *25)
    for k, v in settings.items():
        print(f"{k}: {v}")

configs = {}
print("Enter settings (type 'done' to stop):")

while True:
    key = input("Key: ")
    if key == "done":
        break
    
    value = input("Value: ")
    configs[key] = value

show_config(**configs)


# =================================================
# * Task 4: Factorial Service (Recursion) ***********
def factorial(n):
    if n < 0:
        return "*Error: No negatives*"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
   num = int(input("Enter a number : "))
   print(f"Result: {factorial(num)}\n")
except :
   print("Error : *please enter numbers only*")



# =================================================
# * Task 5: Memory Optimization (Generator)********
# Generator: Yields one at a time (saves memory)
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

# List: Creates everything at once (takes memory)
def square_list(n):
    return [i * i for i in range(1, n + 1)]

# Simple Input
num = int(input("Enter a number: "))

# 1. The List way
print(f"List: {square_list(num)}")

# 2. The Generator way
gen = square_generator(num)
print("Generator Values:", end=" ")
for val in gen:
    print(val, end=" ")



# =================================================
# * Task 6: Exception Handling Module *************
def divide():
    try:
        # 1. Take input and convert
        num = float(input("Enter numerator: "))
        den = float(input("Enter denominator: "))
        
        # 2. Perform math
        result = num / den
        print(f"Result: {result:.2f}")

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numbers only.")
    finally:
        # This runs NO MATTER WHAT (success or error)
        print("Program Completed")

divide()



# =================================================
# ***Task 7: File Handling**************************

# 1. Create file: team_data.txt and / 2.Write to the file
with open("team_data.txt", "w") as f:
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    
    f.write(f"Name: {name}\nRole: {role}")

print("Data written to the file team_data.txt")

# 3. Read and Display content
print("\n* Reading File Content *")
with open("team_data.txt", "r") as f:
    print(f.read())

# 4. Check if file is closed
print(f"\n Is the file closed? >>{f.closed}")
   
