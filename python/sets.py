e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 

print(s)

m = {1, 5, 32, 54,5, 5, 5, "ronak"}

print(m, type(m))

m.add(566)
print(m, type(m))

m.remove(1)
print(m, type(m))

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))


# Difference -> Elements present in s1 but not in s2
print(s1.difference(s2))
# Output: {45, 6}

# Difference (other way around)
print(s2.difference(s1))
# Output: {7, 8}

# Symmetric Difference -> Elements present in either set but NOT in both
print(s1.symmetric_difference(s2))
# Output: {45, 6, 7, 8}

# Check if s2 is subset of s1
print(s2.issubset(s1))
# Output: False

# Check if s1 is superset of s2
print(s1.issuperset(s2))
# Output: False

# Check if two sets have no common elements
print(s1.isdisjoint(s2))
# Output: False (because 1 and 78 are common)

# Copy
s3 = s1.copy()
print(s3)
# Output: {1, 45, 6, 78}

# Update
s3.update(s2)   # Adds all elements of s2 into s3
print(s3)
# Output: {1, 45, 6, 78, 7, 8}

# Discard
s3.discard(45)  # Removes 45 if present
print(s3)
# Output: {1, 6, 78, 7, 8}

s3.discard(999) # No error if element doesn't exist
print(s3)
# Output: {1, 6, 78, 7, 8}

# Pop
removed = s3.pop()  # Removes a random element
print("Removed:", removed)
# Output: Removed: (Random Element)

print(s3)
# Output: Remaining elements after pop

# Clear
temp = {10, 20, 30}
print(temp)
# Output: {10, 20, 30}

temp.clear()
print(temp)
# Output: set()

# Membership
print(45 in s1)
# Output: True

print(100 in s1)
# Output: False

# Length
print(len(s1))
# Output: 4

# Frozen Set
fs = frozenset({1, 2, 3, 4})
print(fs)
# Output: frozenset({1, 2, 3, 4})

# fs.add(5)
#  Error: frozenset is immutable



# s = set()
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  

# print(s)

intro = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
intro.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
intro.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
intro.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
intro.update({name: lang})


print(intro)
