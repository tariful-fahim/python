courses = ['History', 'CSE', 'Math', 'Physics']
#+ve Index   0         1        2       3
#-ve Index   -4         -3      -2      -1
print(courses)
#Length of List
print(len(courses))
#access the certain value from list
# List[start:end:step]
print(courses[1:3])
print(courses[-1:-4:-1]) #reverse order travers

#add item to the list's last position
courses.append('Art')
courses.append('EEE')
print(courses)

#add item to an specific position of a list
#insert(position,item)
courses.insert(1,'CEP')
print(courses)

#Extend method
#if we want to add item from another list we have to use extend method. if we use 'insert' or 'append'
#method, it will take the whole list into the main list.
courses_2 = ['sociology', 'chemistry']
#courses.append(courses_2)
#print(courses)
courses.extend(courses_2)
print(courses)

#removing element from the list
#remove method
courses.remove('Math')
print(courses)
#pop method. specially remove the last item of the list
popped = courses.pop()
print(popped)
print(courses)

#sorting
#courses.sort()
#print(courses) #ascending order
#courses.sort(reverse=True)
#print(courses)
#sorting the list without alternating the item
sorted_list = sorted(courses) #sorted() function
print(sorted_list)
# max, min, sum function
nums = [2,1,4,6,9]
print(min(nums))
print(max(nums))
print(sum(nums))

#Find the index value of the item
print(courses.index('CSE'))
print('CSE' in courses) # true or false

#accessing the list through the looping

for item in courses:
    print(item)

#enumerate function which return two values, index of the value and the item of that value

for index, item in enumerate(courses, start=1):
    print(index, item)

#List converted to a string and string converted to a list

courses_str = ' - '.join(courses)
new_courses = courses_str.split(' - ')
print(courses_str)
print(new_courses)
