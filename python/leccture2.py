# "", '',"' '" these all three are valid ways to define a string in Python. You can use double quotes, single quotes, or triple quotes (for multi-line strings).
str1 = "Ronak"  
print(str1)
print(len(str1)) # length of the string

str2 = 'Mitali'
print(str2)
print(len(str2)) # length of the string

str3 = "Mituu" + " " + "Ronak" + " " + "se baat nhi kr rhi hai"
#concatenation of strings
print(str3)
print(len(str3)) # length of the string

# intialization of loop : starting value , limit value , increment value
for i in range(1, 10, 2):
    print("Mituuuuuuuuuuuuuuuuuuuuuuuuuuu") # this will print the string 500 times, as it iterates through odd numbers from 1 to 999

#printing numbers with spaces
for i in range(5):
    print(i, end=" ")
# end wale string ko ""null kiya toh yeh print karega 01234


print() # this will print a new line

str4 = "Mitu"
print(str4[0]) # accessing the first character of the string
print(str4[1]) # accessing the second character of the string
print(str4[2]) # accessing the third character of the string
print(str4[3]) # accessing the fourth character of the string  

for i in range(len(str4)):
    print(str4[i], end=" ") # this will print each character of the string on a new line
print()


#slicing of string
str5 = "learning python for ds"
print(str5[:8]) #[no starting idx toh 0idx se start hoga : <limitingidx]
print(str5[9:15]) #[startingidx : <limitingidx]
print(str5[20:]) #[startingidx : no limit toh last idx tak jayega or <len(str)]
print(str5[:8]+" "+str5[9:15]+" "+str5[20:])

#-ve slicing is similar to this bas idx -ve hai


#some impt string function

# Sample String
s = "I am a coder."

# 1. endswith()
# Checks if string ends with given substring

print(s.endswith("er."))   # True
print(s.endswith("coder")) # False


# 2. startswith()
# Checks if string starts with given substring

print(s.startswith("I"))   # True
print(s.startswith("am"))  # False


# 3. capitalize()
# Makes first character uppercase

name = "ronak"
print(name.capitalize())   # Ronak


# 4. upper()
# Converts entire string to uppercase

print(name.upper())        # RONAK


# 5. lower()
# Converts entire string to lowercase

print("RONAK".lower())     # ronak


# 6. title()
# Capitalizes first letter of each word

print("i am ronak".title()) # I Am Ronak


# 7. replace()
# Replaces all occurrences

print(s.replace("coder", "developer"))
# I am a developer.


# 8. find()
# Returns first index of substring
# Returns -1 if not found

print(s.find("am"))        # 2
print(s.find("hello"))     # -1


# 9. index()
# Similar to find()
# Throws error if substring not found

print(s.index("coder"))    # 7


# 10. count()
# Counts occurrences

text = "am am am"
print(text.count("am"))    # 3


# 11. strip()
# Removes spaces from both ends

x = "   hello   "
print(x.strip())           # hello


# 12. lstrip()
# Removes left spaces

print(x.lstrip())          # hello___


# 13. rstrip()
# Removes right spaces

print(x.rstrip())          # ___hello


# 14. split()
# Converts string into list

sentence = "apple banana mango"
print(sentence.split())

# ['apple', 'banana', 'mango']


# 15. join()
# Joins list into string

arr = ["I", "am", "Ronak"]

print(" ".join(arr))
# I am Ronak


# 16. isalpha()
# Checks if all characters are alphabets

print("Ronak".isalpha())   # True
print("Ronak123".isalpha())# False


# 17. isdigit()
# Checks if all characters are digits

print("123".isdigit())     # True
print("12a".isdigit())     # False


# 18. isalnum()
# Checks letters + digits only

print("Ronak123".isalnum()) # True
print("Ronak@123".isalnum())# False


# 19. swapcase()
# Upper -> Lower
# Lower -> Upper

print("RoNaK".swapcase())
# rOnAk


# 20. len()
# Length of string

print(len("Ronak")) # 5

print()
name = input("enter yout name : ")
print("length of the your name is :",len(name))
print()
print()

# learning if-elif-else :

# Simple if
age = 20

if age >= 18:
    print("You can vote")


# If else
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# If elif else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Multiple if
num = 12

if num > 0:
    print("Positive")

if num % 2 == 0:
    print("Even")


# Nested if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")


# AND
if age >= 18 and has_id:
    print("Allowed")


# OR
marks = 95
sports = False

if marks >= 90 or sports:
    print("Scholarship Eligible")


# NOT
logged_in = False

if not logged_in:
    print("Please Login")


# Even Odd
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Positive Negative Zero
num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Uppercase
ch = "A"

if ch.isupper():
    print("Uppercase")
else:
    print("Not Uppercase")


# Lowercase
ch = "r"

if ch.islower():
    print("Lowercase")
else:
    print("Not Lowercase")


# Digit
ch = "7"

if ch.isdigit():
    print("Digit")
else:
    print("Not Digit")


# Leap Year
year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")


# Vowel Consonant
ch = "a"

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


# Largest of two
a = 10
b = 20

if a > b:
    print("a is larger")
else:
    print("b is larger")


# Largest of three
a = 10
b = 20
c = 15

if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")


# Ternary Operator
age = 17

result = "Adult" if age >= 18 else "Minor"

print(result)


# Menu Program
choice = 2

if choice == 1:
    print("Pizza")
elif choice == 2:
    print("Burger")
elif choice == 3:
    print("Pasta")
else:
    print("Invalid Choice")


# User Input Example
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ==    Equal
# !=    Not Equal
# >     Greater Than
# <     Less Than
# >=    Greater Than Equal
# <=    Less Than Equal

