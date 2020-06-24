import sys
#importing another file
import my_module 
print('process number 1')
print(my_module.Test)

m = 8
my_module.mul(m)

#importing file with shorthand name

import my_module as mm
print('process number 2')
print(mm.Test)

m = 8
mm.mul(m)

#importing certain function from a file

from my_module import Test,mul
print('process number 3')
print(Test)
m = 5
print(mul(m))

#importing all the function from a File

from my_module import *
print('process number 4')
print(Test)
m = 4
print(mul(m))

print(sys.path)

#importing random, math, os file

import random, math, os, datetime, calendar

nums = [2,5,2,4,2,1]

rand = random.choice(nums)
print(rand)

rad = math.radians(90)
print(math.sin(rad))

today = datetime.date.today()
print(today)

print(os.getcwd())
print(os.__file__)