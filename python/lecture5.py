# loops in python 

# i = 1
# while i<=10:
#     print(i)
#     i += 1

# j = 10
# while j>=1:
#     print(j)
#     j -= 1


# m = 1
# n = int(input("enter number :"))
# while(m<=10):
#     print (n*m)
#     m += 1

# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx<len(nums):
#     print(nums[idx])
#     idx += 1

nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i<len(nums):
     if(nums[i] == x):
      print("found at index :",i)
     i += 1
     