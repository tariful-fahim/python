
# key-vale pair
student = {'name':'john', 'Roll':42, 'course':['Math','DS']}
print(student['name'])

#When we use wrong key (doesn't exist on the dictonaries) in the third bracket we get an error.
#But we can print out as our expectation by using 'get' method

#get method

print(student.get('phone', 'Not Found'))

#Adding new key to the Dictionaries
# Normal way
student['phone'] = '019xxxx'
student['name'] = 'dhonu' #updatig the name
print(student)

#update method
student.update({'phone':'018xxx', 'age':26})
print(student)

#Delete keys from the Dictionaries

#del method

del student['phone']
print(student)

#pop method
# In Dictionaries 'pop' method expect at least one argument.

age = student.pop('age');
print(age)


#number of keys
print(len(student))

#print the keys, values, and pair of key-valu of dictionaries
print(student.keys())
print(student.values())
print(student.items())

#loop through the keys and values

for key, value in student.items():
    print(key, value)
