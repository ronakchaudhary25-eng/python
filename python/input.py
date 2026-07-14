name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
complex_num = complex(input("Enter a complex number (e.g., 2+3j): "))
numbers_list = list(map(int, input("Enter numbers separated by space: ").split()))
numbers_tuple = tuple(map(int, input("Enter numbers for tuple: ").split()))
numbers_set = set(map(int, input("Enter numbers for set: ").split()))

student = {}
student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter student age: "))

print("\n===== OUTPUT =====")

print("Name:", name)
print("Type:", type(name))

print("\nAge:", age)
print("Type:", type(age))

print("\nHeight:", height)
print("Type:", type(height))

print("\nIs Student:", is_student)
print("Type:", type(is_student))

print("\nComplex Number:", complex_num)
print("Type:", type(complex_num))

print("\nList:", numbers_list)
print("Type:", type(numbers_list))

print("\nTuple:", numbers_tuple)
print("Type:", type(numbers_tuple))

print("\nSet:", numbers_set)
print("Type:", type(numbers_set))

print("\nDictionary:", student)
print("Type:", type(student))
