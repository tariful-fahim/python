
num = 7

if num<0:
    print("Negative Number")
elif num > 0:
    print("postive numebr")
else:
    print("zero number")

#and, or, not

user = 'Admin'
logged_in = 'True'

if user == 'Admin' or logged_in:
    print("Admin page")
else:
    print("not admin")

# object identity 'is' to check wether two objects are in the same memory or not

a = [1,2,3]
b = a

print(id(a))
print(id(b))

print(a is b)

# False condition by default

#False
#None
#Zero of any numeric type
#An empty sequence.. (), [], ''
#An empty mapping.. {}