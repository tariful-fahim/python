#Mutable

List_1 = ['CSE', 'CEP', 'EEE', 'IPE']
List_2 = List_1;

print(List_1)
print(List_2)

List_1[3] = 'Bangla'
print(List_1)
print(List_2)

#Immutable

tuples_1 = ('CSE', 'CEP', 'EEE', 'IPE')
tuples_2 = tuples_1

print(tuples_1)
print(tuples_2)

# tuples_1[3] = 'Bangla'  tuples object doesn't support item assignment because it is immutable. most of
# the list method doesn't work at tuple..
print(tuples_1)
print(tuples_2)


#SET
#unordered and doesn't support the duplicate value
courses_1 = {'CSE', 'EEE', 'CEP', 'STAT', 'IPE', 'IPE'}
print(courses_1)

# Intersection, Union, Difference method between two sets
courses_2 = {'Art','EEE','Bangla','STAT','CEP'}
print(courses_1.intersection(courses_2))
print(courses_1.union(courses_2))
print(courses_1.difference(courses_2))

#we can combined set using mathematical expression
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

#Empty list
empty_list = []
#or
empty_list = list()

#Empty tuple
empty_tuple = ()
#or
empty_tuple = tuple()

#Empty set
#empty_set = {} #this isn't right. it creates dictionary.
#or
empty_tuple = tuple()