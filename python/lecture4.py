# lets begin learning dictionary in python
# (right side of =) are the values of the keys(left of =) and right side can be of any daya type 
#  dictionaries are mutable i.e we can modify 
info = {
    "key" : "Ronak Chaudhary",
    "Hobby" : "coding , playing sports",
    "age" : "19",
    "marks" : "9.2cgpa"
}
print(info)
print(type(info))
print(info["key"])
print(info["Hobby"])

null_dict = {}
print(null_dict)
null_dict["College"] = "SPIT"
print(null_dict)

# nested dictionary
stud = {
    "naam" : "Ronak Mitali",
    "subj" : {
     "phy" : 100,
     "chem" : 100,
     "maths" : 96
    }
    }
#  printing specific marks of the subject
print(stud["subj"]["chem"])
#  stud.keys() this will only print keys of parent dict not nested dict ka keys
print(stud.keys())
# printing list of keys
print(list(stud.keys()))
print(len(list(stud.keys())))
print(stud.values())
print(list(stud.values()))
#  to print key and value corresponding of dictionary together use .items
print(stud.items())
print(list(stud.items()))

pairs = list(stud.items())
print(pairs[0])
print(pairs[1])

# set :
#  sets are mutable but its elements are immutable
collection = {1,2,3,"hello","hello","world",4}
print(type(collection))
print(collection)

# empty dictionary not empty set
collect = {}
print(type(collect))

# empty set intialization 
col = set()
print(type(col))

# methods in set :
st = set()
st.add(1)
st.add(2)
st.add(2)
print(st)
st.remove(2)
print(st)

print(len(collection))
collection.clear()
print(len(collection))

set1 = {1,2,3}
set2 = {1,2,5,6}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))

score = {}

x = int(input("enter score of phy :"))
score.update({"phy" : x})

x = int(input("enter score of chem :"))
score.update({"chem" : x})

x = int(input("enter score of maths :"))
score.update({"maths" : x})

print(score)
