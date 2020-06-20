# printing multiple line in a string
message="""pyhton is a much much
easier language to understand"""  

message1 = "what an interesting match"
# length of the string
print(len(message1))
#printing the certain string
print(message1[:])
print(len(message))

# upper and lower method
print(message1.upper())
print(message1.lower())

#count the number of words in a string
print(message1.count('i'))

#find method
print(message1.find('in'))

#replace method
print(message1.replace('match','player'))

#concatenate
print(message1+' such a thriller match i have ever seen')

#string format
greeting = 'Hello'
name = 'bojak'
check = f'{greeting},{name}. Welcome!'
print(check)

# DIR and HELP method
print(dir(str))
print(help(str.lower))