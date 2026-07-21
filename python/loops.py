# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

for i in range(1,10):
    print(i)


# i = 1
# while(i<51):
#     print(i)
#     i +=1 

# l = [1, "ronak", False, "mukund", "Rohan", "mitali", "moky"]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i += 1

# for i in range(5):
#     print(i)

# L = [1,24,5,6,7443,563,0]
# for i in L:
#     print(i)

# t = ("ronak",45,18,66)
# for i in t:
#     print(i)

# s = "ronak"
# for i in s :
#     print(i)

# m= [1,7,8,18,45,0,-1] 
# m.sort()
# for item in m:
#     print(item)

# else:
#     print("done") # exits!

# for i in range(100):
#     if(i == 18):
#         break # Exit the loop right now!!
#     print(i)

# for i in range(100):
#     if(i == 45):
#         continue # Skips current iteration
#     print(i)    

# n = int(input("enter a number :"))
# for i in range(1,11):
#     print(f"{n}x{i} = {n*i}")
#     pass

# print("table printed")



# m = int(input("enter a number :"))
# for i in range(2,m):
#     if(m%i==0):
#         print("number is not prime!!")
#         break
#     else :
#         print(" yoo bro gott !! prime")
#         break


n = int(input("enter a number :"))
fact = 1
for i in range(2,n+1):
    fact *= i

print(f"the factorial on {n} is {fact}")
