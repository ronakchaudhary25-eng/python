# LIST

nums = [10, 20, 30]

# Add one element at end
nums.append(40)
print(nums)

# Add multiple elements
nums.extend([50, 60])
print(nums)

# Insert at specific index
nums.insert(2, 25)
print(nums)

# Remove first occurrence
nums.remove(20)
print(nums)

# Remove last element
last = nums.pop()
print(nums)
print(last)

# Remove element at index
removed = nums.pop(1)
print(nums)
print(removed)

# Count frequency
nums.append(30)
print(nums.count(30))

# First occurrence index
print(nums.index(30))

# Sort ascending
nums.sort()
print(nums)

# Sort descending
nums.sort(reverse=True)
print(nums)

# Reverse current list
nums.reverse()
print(nums)

# Copy list
copy_list = nums.copy()
print(copy_list)

# Clear list
temp = [1, 2, 3]
temp.clear()
print(temp)

arr = [5, 2, 9, 1]

# Length
print(len(arr))

# Maximum
print(max(arr))

# Minimum
print(min(arr))

# Sum
print(sum(arr))

# Returns sorted copy
print(sorted(arr))
print(arr)

# Membership
print(2 in arr)
print(100 not in arr)

# Slicing
print(arr[:])
print(arr[1:3])
print(arr[:2])
print(arr[2:])
print(arr[::-1])


# TUPLE

t = (10, 20, 30, 20)

# Count frequency
print(t.count(20))

# First occurrence index
print(t.index(30))

# Built-in functions
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

# Membership
print(20 in t)

# Loop
for x in t:
    print(x)

# Slicing
print(t[:])
print(t[1:3])
print(t[::-1])


# BONUS (Very useful for DSA)

nums = [4, 2, 7, 1]

# enumerate()
for index, value in enumerate(nums):
    print(index, value)

# zip()
a = [1, 2, 3]
b = ['A', 'B', 'C']

for x, y in zip(a, b):
    print(x, y)

# Tuple unpacking
x, y, z = (100, 200, 300)
print(x, y, z)

# List comprehension
square = [i * i for i in range(5)]
print(square)