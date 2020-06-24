#For loop

nums = [3,4,5,6,3]

for i in nums:
    if(i%2 == 0):
        print(i,'even')
    else:
        print(i,'odd')
#range
for i in range(len(nums)):
    print(nums[i])

#While loop

x = 0
while x < 20:
    print(x)
    x+=1