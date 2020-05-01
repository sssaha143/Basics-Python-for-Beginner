# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 21:16:51 2019

@author: Subhajit saha

Python Tutorial for Beginners 4: Lists, Tuples, and Sets
"""

Fruits = ['Mango','Orange','Apple','Banana']

print(Fruits[1])
Fruits.append('berry')

#print(Fruits)

Fruits.insert(1, 'Gauva') # 1 is the location where to be place item
#print(Fruits)

car = ['Maruti', 'TATA']
Fruits.extend(car)
#print(Fruits)

Fruits.remove('TATA')
#print(Fruits)

Fruits.pop()
popped = Fruits.pop()
print(popped)

Fruits.reverse()
Fruits.sort()
#print(Fruits)

Num = [1,6,3,5,7,2]
Num.sort(reverse=True)
sorted_num = sorted(Num)

print(sorted_num)

#print(min(Num))
#print(max(Num))
print(sum(Num))

#print(Fruits.index('Apple'))

#print('Apple' in Fruits) # its will ans in true & false

#for item in Fruits:
#    print(item)

for index, item in enumerate(Fruits):
    print(index, item)
 
fruits_str = ' , '.join(Fruits) # Join method ex. fruits_str = '-'.join(Fruits)
print(fruits_str)   

Fruit_list = fruits_str.split(' , ')
print(Fruit_list)

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

art_courses = {'History', 'CompSci', 'Arts', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()