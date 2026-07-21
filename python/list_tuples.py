bro = ["hii","bye",74,86.3,7]
print(bro)
bro.append("Rronak!!")
print(bro)

L = [1,23,13,0,-1]
# L.sort()
# L.reverse
L.insert(2,4552)
L.pop(2)
print(L)
print(L.pop(2))

#  string immuatable ,tuple immutable , list mutable -> stl !!!
#  tuple : 

a = (1,) # single element tuple !
b = (1,2,2,5,"ronak","broski")
print(a)
print(b)
print(type(b))

print(b.count(5))
print(b.index("ronak"))

marks = []
m1 = int(input("enter marks of 1st student : "))
marks.append(m1)
m1 = int(input("enter marks of 2nd student : "))
marks.append(m1)
m1 = int(input("enter marks of  3rd student : "))
marks.append(m1)
m1 = int(input("enter marks of 4th student : "))
marks.append(m1)
m1 = int(input("enter marks of 5th  student : "))
marks.append(m1)
marks.sort()
print(marks)
print(sum(marks))
