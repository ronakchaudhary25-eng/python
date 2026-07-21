#  dictionaries are unoredered , mutable , indexed , unique keys
marks = {
    "ronak" : 100,
    "moky" : 100,
    "mukund" : 100,
    100 : "rohan"
}
empty = {}
#  empty set :
# e = set()


print(type(empty))

print(marks , type(marks))
print(marks["ronak"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"ronak":99}) #mutable !!
print(marks)

print(marks.get("ronak1"))#prints none
print(marks["ronak1"])#return error
