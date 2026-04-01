# Task 1: Encapsulation (User Class)

class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    # Create
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name  # password intentionally hidden

    # Add
    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


user = User()
user.set_user("john", "john123")

user.register()
user.login()

# ===========================================================
# Task 2: Inheritance (User → Student, Faculty)

# Parent class
class User:
    def register(self):
        print("User registered.")

    def login(self):
        print("User logged in.")


# Single inheritance
# Student
class Student(User):
    def student_greet(self):
        print("Hello Student")

# Faculty
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


# Multilevel inheritance
# TempFaculty (Multilevel)
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


print("---- Student ----")
s = Student()
s.register()          
s.login()             
s.student_greet()   

print("\n---- Faculty ----")
f = Faculty()
f.register()     
f.login()       
f.faculty_greet()    

print("\n---- TempFaculty ----")
tf = TempFaculty()
tf.register()    
tf.login()         
tf.faculty_greet()  
tf.tempFaculty_greet() 

print("\n---- Parent cannot reach child---- ")
u = User()
u.register()
# u.student_greet()
print("u.student_greet() would raise AttributeError")

# ====================================================
# Task 3: Method Overriding

# Parent
class User:
    def greet(self):
        print("Welcome User")

# Student
class Student(User):
    def greet(self):            
        print("Welcome Student")

# Faculty
class Faculty(User):
    def greet(self):          
        print("Welcome Faculty")


# Demo
u = User()
s = Student()
f = Faculty()

u.greet() 
s.greet()  
f.greet()  

# Polymorphism
print("\n--- Loop demo (polymorphism) ---")
for person in [u, s, f]:
    person.greet()

# Accessing the parent from inside the child
print("\n--- Calling parent greet() via super() ---")
class Student2(User):
    def greet(self):
        super().greet()      
        print("Welcome Student")

Student2().greet()

# ===================================================
# Task 4: Method Chaining


class User:

    # Methods:
    # register()
    def register(self):
        print("registered")
        return self  
    
    # login()
    def login(self):
        print("logined")
        return self    
    
    # greet()
    def greet(self):
        print("greet enjoy everyone")
        return self    

# Method chaining
user = User()
user.login().greet().register()