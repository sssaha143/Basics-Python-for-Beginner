# -*- coding: utf-8 -*-
"""
Python Practice
"""
"""
@author: subhajit saha
"""
"""
Python Tutorial: Slicing Lists and Strings
"""

list = [0,1,2,3,4,5,6,7,8,9]
#       0,1,2,3,4,5,6,7,8,9
#      -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list = [start:end:step]
print(list[9:2:-2])
print(list[0:5])
print(list[::-1])
print(list[0::-2])

string = 'https://google.com'

print(string)
print(string[-4::])
print(string[8:-4])

"""
Strings - Working with Textual Data
"""
massege = "hello world"
print(massege)
print(len(massege))
print(massege[0:4])
print(massege[0:4:5])
m = massege
print(m.capitalize())
print(m.upper())
print(m.count('o'))
print(m.find('w'))

subhajit = m.replace('world','subhajit')
print(m.replace('world','subhajit'))
print (subhajit)

greetings = 'namaste'
name = 'shubh'
g = greetings + ', ' + name #easy way
print(g)
G = '{}, {}. welcome!'.format(greetings,name) # send way
print(G)
Gg = f'{greetings}, {name.upper()}. welcome!' # called f string
print(Gg)
#print(dir(name)) to know the available command on represent string
#print(help(str.endswith)) its a kind of dictonary of command


"""
Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates

"""
person = {'name' : 'shubh','age' : '25'}
pl = '1 My name is ' + person['name'] + '. & age is ' + person['age']
print(pl) 
pl = '2 My name is {} & age is {}'.format(person['name'],person['age'])
print(pl)
pl = '3 My name is {0} & age is {1}'.format(person['name'],person['age'])
print(pl)
pl = '4 My name is {0[name]} & age is {1[age]}'.format(person,person)
print(pl)
pl = '5 My name is {0[name]} & age is {0[age]}'.format(person)
print(pl)

l = ['shubh','25']
pl = '6 My name is {0[0]} & age is {0[1]}'.format(l)
print(pl)
pl = '7 My name is {name} & age is {age}'.format(name='shubh',age='25')
print(pl)
pl = '8 My name is {name} & age is {age}'.format(**person)
print(pl)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

tag = 'hi'
text = 'i have a html code'
html = '<{0}>{1}</{0}>'.format(tag,text)
print(html)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
pl = Person('shubh','25')
p = '9 My name is {0.name} & age is {0.name}'.format(pl)
print(p)   

#####formating the looping through a number

for i in range(1,11):
    sentence = 'The value is {:04}'.format(i)
    print(sentence)

pi = 3.14152965
print('the value of pi is {:.4f}'.format(pi)) 

print('1mb is equal to {}'.format(1000**2))
print('1mb is equal to {:,}'.format(1000**2))
print('1mb is equal to {:,.02f}'.format(1000**2))

##### formating a DateTime
import datetime
mydate = datetime.datetime(2019,12,16,12,58,23)
print(mydate)
my_date = '{:%B %d, %Y}'.format(mydate)
print(my_date)
my_date = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(mydate)
print(my_date)
