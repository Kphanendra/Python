# Task 1: Use super() properly

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"  Name : {self.name}")
        print(f"  ID   : {self.id}")


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def display(self):
        super().display()
        print(f"  Dept : {self.dept}")
        print(f"  Fees : ₹{self.fees}")


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def display(self):
        super().display()
        print(f"  Salary : ₹{self.salary}")


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def display(self):
        super().display()
        print(f"  Duration : {self.duration} months")


s = Student("Phani", "S101", "Computer Science", 5000)
f = Faculty("Kumar", "F201", 90000)
tf = TempFaculty("Amith", "TF301", 60000, 5)

print("\n Student")
print("=" * 25)
s.display()

print("\n Faculty")
print("=" * 25)
f.display()

print("\n TempFaculty")
print("=" * 25)
tf.display()
print("─" * 25)

# ===================================================

# Task 2: Apply Abstraction

from abc import ABC, abstractmethod

class AbstractUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def get_details(self):
        pass


class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return (
            f" #[Student]\n"
            f"  Name : {self.name}\n"
            f"  ID   : {self.id}\n"
            f"  Dept : {self.dept}\n"
            f"  Fees : ₹{self.fees}")


class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return (
            f"#[Faculty]\n"
            f"  Name   : {self.name}\n"
            f"  ID     : {self.id}\n"
            f"  Salary : ₹{self.salary}")


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        base = super().get_details().replace("[Faculty]", "[TempFaculty]")
        return base + f"\n  Duration : {self.duration} months"


# ── Demo
users = [
    Student("Phani", "S101", "Computer Science", 75000),
    Faculty("Kumar", "F201", 90000),
    TempFaculty("Sumith", "TF301", 60000, 6),
]

for user in users:
    print("─" * 25)
    print(user.get_details())
print("─" * 25)

# ===============================================================

# Task 3: Sorting using key

class Student:
    def __init__(self, name, dept, fees):
        self.name = name
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} ({self.dept}) - ₹{self.fees}"


class Faculty:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def __repr__(self):
        return f"{self.name} ({self.dept}) - ₹{self.salary}"


# ── Collage Data
students = [
    Student("Phani", "CSC",    500000),
    Student("Kumar",  "EEE",  400000),
    Student("Amith",  "ECE",   450000),
    Student("Sumith", "EEE",   400000),
    Student("Jani", "CSC",    500000),
    Student("Arya",  "ECE",   450000),]

faculty = [
    Faculty("Pr. Surya",  "ECE",   75000),
    Faculty("Pr. Ajith",  "CSC",   85000),
    Faculty("Pr. Vijay", "EEE",   60000),]


students.sort(key=lambda x: x.fees)
print("Sorted students by fees (Asending):")
for s in students:
    print(" ", s)


faculty.sort(key=lambda x: x.salary, reverse=True)
print("\n sorted Faculty by salary (Decending):")
for f in faculty:
    print(" ", f)

# ==============================================================

# Task 4: Use map()

class Student:
    def __init__(self, name, dept, fees):
        self.name = name
        self.dept = dept
        self.fees = fees


students = [
    Student("Phani", "CSC",    500000),
    Student("Kumar",  "MECH",  400000),
    Student("Amith",  "ECE",   450000),
    Student("Sumith", "EEE",   400000),]

# Extract names
names = list(map(lambda s: s.name, students))
print("Names:", names)

# Extract fees
fees = list(map(lambda s: s.fees, students))
print("Fees:", fees)

# ================================================================

# Task 5: Use filter()

class Student:
    def __init__(self, name, dept, fees):
        self.name = name
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} ({self.dept}) - ₹{self.fees}"


class Faculty:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def __repr__(self):
        return f"{self.name} ({self.dept}) - ₹{self.salary}"


students = [
    Student("Phani",  "CSC",   50000),
    Student("Kumar",  "MECH",  65000),
    Student("Amith",  "ECE",   45000),
    Student("Sumith", "EEE",   60000),]

faculty = [
    Faculty("Pr. Surya",  "ECE",   35000),
    Faculty("Pr. Ajith",  "CSC",   25000),
    Faculty("Pr. Vijay", "EEE",    30000),]

# Students with fees > 50000
high_fee = list(filter(lambda s: s.fees > 50000, students))
print("*Students fees 50000:")
print("─" * 25)
for s in high_fee:
    print(" ", s)

# Faculty with salary > 30000
high_salary = list(filter(lambda f: f.salary > 30000, faculty))
print("\n*Faculty salary > 30000:")
print("─" * 25)
for f in high_salary:
    print(" ", f)

# ==============================================================

# Task 6: Use reduce()

from functools import reduce

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

students = [
    Student("Phani", 75000),
    Student("Kumar", 50000),
    Student("Ajay",  60000),
    Student("Vijay", 90000),]

faculty = [
    Faculty("Pr. Amith",  95000),
    Faculty("Pr. Sumith", 25000),
    Faculty("Pr. Surya",  85000),
    Faculty("Pr. John",   30000),]


# Total salary of all faculty
print("─" * 25)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)
print("Total salary paid    : ₹", total_salary)

# Total fees collected
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
print("Total fees collected : ₹", total_fees)
print("─" * 25)

# ===============================================================

# Task 7: Higher Order Function

class Student:
    def __init__(self, name, dept, fees):
        self.name = name
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} ({self.dept}) - ₹{self.fees}"


# Higher Order Function
def process_users(users, func):
    return list(map(func, users))


students = [
    Student("Phani",  "CSC",   50000),
    Student("Kumar",  "MECH",  65000),
    Student("Amith",  "ECE",   45000),
    Student("Sumith", "EEE",   60000),]


# Extract names
names = process_users(students, lambda s: s.name)
print("Names:", names)

# Extract fees
fees = process_users(students, lambda s: s.fees)
print("Fees :", fees)

# ============================================================

# mini system:

from abc import ABC, abstractmethod
from functools import reduce

# Abstract Base 
class AbstractUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def get_details(self):
        pass

# Classes 
class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"  {self.name:<12} | ID: {self.id} | Dept: {self.dept:<8} | Fees: ₹{self.fees}"


class Faculty(AbstractUser):
    def __init__(self, name, id, dept, salary):
        super().__init__(name, id)
        self.dept = dept
        self.salary = salary

    def get_details(self):
        return f"  {self.name:<12} | ID: {self.id} | Dept: {self.dept:<8} | Salary: ₹{self.salary}"


# Higher Order Function 
def process_users(users, func):
    return list(map(func, users))

# College Data 
students = [
    Student("Phani", "S101", "CSC",   50000),
    Student("Kumar", "S102", "MECH",  65000),
    Student("Amith",  "S101", "ECE",   45000),
    Student("Sumith", "S101", "EEE",   60000),]

faculty = [
    Faculty("Pr. Surya", "F101",  "ECE",   35000),
    Faculty("Pr. Ajith", "F102",  "CSC",   25000),
    Faculty("Pr. Vijay", "F103", "EEE",    30000),]


sep = "─" * 55

# 1. All Details 
print(" ALL STUDENTS")
print(sep)
for s in students:
    print(s.get_details())

print("\n ALL FACULTY")
print(sep)
for f in faculty:
    print(f.get_details())

# 2. Sorted Data 
print("\nSTUDENTS — sorted by fees Asending")
print(sep)
sorted_students = sorted(students, key=lambda s: s.fees)
for s in sorted_students:
    print(s.get_details())

print("\n FACULTY — sorted by salary Decending")
print(sep)
sorted_faculty = sorted(faculty, key=lambda f: f.salary, reverse=True)
for f in sorted_faculty:
    print(f.get_details())

# 3. Filtered Data
print("\n STUDENTS — fees > ₹50000")
print(sep)
high_fee = list(filter(lambda s: s.fees > 50000, students))
for s in high_fee:
    print(s.get_details())

print("\n FACULTY — salary > ₹30000")
print(sep)
high_salary = list(filter(lambda f: f.salary > 30000, faculty))
for f in high_salary:
    print(f.get_details())

# 4. map() via Higher Order Function 
print("\n STUDENT NAMES (via process_users + map)")
print(sep)
names = process_users(students, lambda s: s.name)
print(" ", names)

# 5. Totals via reduce() 
total_fees   = reduce(lambda acc, s: acc + s.fees,   students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty,  0)

print("\n TOTALS")
print(sep)
print(f"  Total fees collected : ₹{total_fees}")
print(f"  Total salary paid    : ₹{total_salary}")
print(f"  Net balance          : ₹{total_fees - total_salary}")
print(sep)