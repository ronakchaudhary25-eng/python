s="Hello, Python!"

# slicing
# slicing type/meaning
# output 

print(s[:])
# Entire string.
# Hello, Python!

print(s[0:5])
# Index 0 to 4.
# Hello

print(s[:5])
# Beginning to index 4.
# Hello

print(s[7:])
# Index 7 to end.
# Python!

print(s[-6:])
# Last 6 characters.
# ython!

print(s[:-7])
# Everything except the last 7 characters.
# Hello,

print(s[::2])
# Every 2nd character.
# Hlo yhn

print(s[1::2])
# Every 2nd character starting from index 1.
# el,Pto!

print(s[::-1])
# Reverses the string.
# !nohtyP ,olleH

print(s[::-2])
# Reverse and print every 2nd character.
# !otP,e

print(s[2:10])
# Index 2 to 9.
# llo, Pyt

print(s[2:10:2])
# Every 2nd character from index 2 to 9.
# lo y

print(s[-10:-3])
# Index -10 to -4.
# lo, Pyt

print(s[-10:-3:2])
# Every 2nd character from index -10 to -4.
# loP

print(s[::3])
# Every 3rd character.
# Hl t!

print(s[5:])
# Index 5 to end.
# , Python!

print(s[:8])
# Beginning to index 7.
# Hello, P

print(s[-1])
# Last character.
# !

print(s[-5:-1])
# Index -5 to -2.
# thon

print(s[3:3])
# Empty string.
#
