# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 01:10:03 2019

@author: subhajit saha
"""

"""
Integers and Floats - Working with Numeric Data
"""

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2


print (3+1)
print (3-1)
print (3 * 1)
print (3/1)
print (3//1)
print (3 ** 1)
print (3%1)
num = 2
num += 2
print (num)
print (abs(-3)) #absolute value
print (round(3.75)) #round function
print (round(3.73, 1)) # this round function to give nearest roundup number

"""
Comparisons oprerators
Output always in Boolen
"""
Num_1 = 10
Num_2 = 20
print (Num_1 == Num_2)
print (Num_1 != Num_2)
print (Num_1 > Num_2)
print (Num_1 < Num_2)
print (Num_1 >= Num_2)
print (Num_1 <= Num_2)

#---------------------------------------------------------------------------#

a = '10'
b = '20'
print(a+b)
a = int(a)
b = int(b)
print(a+b)