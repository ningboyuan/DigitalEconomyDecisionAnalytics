"""
Python Basic Syntax and Data Structure Introduction

Author: Junjie Hu
Created time: 
"""

"""
numeric operation
"""
"""
Basic operations:
+, -, *, /, %, **, //
"""

a = 5
b = 3
a *= 2  # 10
round(a / b, 4)  # 3.3333

c = '10'
d = '20'
e = c + d  # '1020'
f = int(c) + int(d)  # 30

"""
Python provides a straight way for numerical operations
Try comparison operationsL
==,<,<=,>,>=,!=
"""

a = 5
print(a == 5)  # True

print(a <= 5)  # True
print(a < 5)  # False

a = 'A'
b = 'B'
print(a == b)  # False
print(a != b)  # True



"""
string
"""
"""
String is a basic type in python, it's common used and very powerful
"""

welcome_list = ['Welcome', 'to', 'Python', 'World.', 'It\'s', 'Amazing']
# using back slash to escape the single quote.

# using for loop to iterate all elements in the list.
for word in welcome_list:
    print(word)

# a string is also an object, using the join method to connect all the words in the list.
welcome_sentence = ' '.join(welcome_list)

# slicing string by indices.
welcome_sliced = welcome_sentence[0:10]
# try changing the indices to negative.

# see other methods of string object, like:
welcome_upper_case = welcome_sentence.upper()
# by using dir() function, or help() function
dir(str)
# or a str instance
dir(welcome_upper_case)
# likewise,
help(str)

# formatting string
greeting = 'Hallo'
name = 'Jon'
# using format method
print('{}, {}. '.format(greeting, name.upper()) + welcome_sentence)
# using f string, you can write variable name into brackets, directly.
print(f'{greeting}, {name.capitalize()}. ' + welcome_sentence)

"""
tuple and set
"""
"""
tuple and set are two basic structures with different features to list.
"""

# tuple
# Similar to list, but immutable
personal_list = ['Jon Dow', '06-04-2000', 'Male', 'U.S.A']
personal_tuple = ('Jon Dow', '06-04-2000', 'Male', 'U.S.A')
personal_list[0] = 'Allan Lee'  # ['Allan Lee', '06-04-2000', 'Male', 'U.S.A']
personal_tuple[0] = 'Allan Lee'  # tuple' object does not support item assignment

# set
# "Janpan" shown twice
countries_1 = {'China', 'Japan', 'Japan', 'Korea', 'Russia', 'Singapore', 'Turkey'}
countries_2 = {'France', 'Germany', 'Italy', 'Russia', 'Spain', 'Turkey', 'UK', 'USA'}

print(f'Totally {len(countries_1)} countries: {countries_1}')  # sets will drop duplicated elements automatically

# Operation of set
count_inter = countries_1.intersection(countries_2)  # {'Russia', 'Turkey'}
count_1_diff = countries_1.difference(countries_2)  # {'China', 'Japan', 'Korea', 'Singapore'}
count_2_diff = countries_2.difference(countries_1)  # {'France', 'Germany', 'Italy', 'Spain', 'UK'}
countries_new = countries_1.union(countries_2)  # merge two sets into 1 and without duplicates

"""
list
"""
"""
Using list makes Python code simple.
"""

natr_language = ['English', 'German', 'Chinese']
prog_language = ['C++', 'Java', 'C#']

# how many elements in a list?
len(natr_language)  # 3
# how many elements in a string?
len(natr_language[0])  # 7

# adding elements into the list
# append() allows you to add 1 element at the end of the list
natr_language.append('Spanish')  # ['English', 'German', 'Chinese', 'Spanish']

# insert() allows you to add 1 element at arbitrary place
prog_language.insert(0, 'Python')  # ['Python', 'C++', 'Java', 'C#']

# extend() allows you to add multiple elements at the end of the list
python = ['python 2.7', 'python 3.6', 'python 3.7', 'python 3.8']
prog_language.append(python)  # ['Python', 'C++', 'Java', 'C#', ['python 2.7', 'python 3.6']]
more_language = ['Japanese', 'Korean']
natr_language.extend(more_language)  # ['English', 'German', 'Chinese', 'Spanish', 'Japanese', 'Korean']

# remove elements
prog_language.remove(python)  # ['Python', 'C++', 'Java', 'C#']
natr_language.pop(-1)  # 'Korean' pops out. ['English', 'German', 'Chinese', 'Spanish', 'Japanese']
del prog_language[-1]  # ['Python', 'C++', 'Java']

# reorder in list
numbers = [43, 11, 32, 95, 22]
numbers.reverse()  # [22, 95, 32, 11, 43]
numbers.sort()  # [11, 22, 32, 43, 95]
numbers.sort(reverse=True)  # [95, 43, 32, 22, 11]
sorted_number = sorted(numbers)  # sorted function can return a new list instead of altering the original list

print(f'Reverse Numbers: {numbers.reverse()}')  # [22, 95, 32, 11, 43]
print(f'Sort Numbers: {numbers.sort()}')  # [11, 22, 32, 43, 95]
print(f'Reversed Sorting{numbers.sort(reverse=True)}')  # [95, 43, 32, 22, 11]


# basic search in list
min_num = min(numbers)  # 11
max_num = max(numbers)  # 95
sum_num = sum(numbers)  # 203
index_num = numbers.index(32)  # 2

# iterate in list
for lang in prog_language:
    print(lang)
# iterate in list with index
for num, lang in enumerate(natr_language):
    print(f'{num}. {lang}')

# list to string
natr_language_str = ', '.join(natr_language)  # 'Spanish, Japanese, German, English, Chinese'
natr_language_new = natr_language_str.split(', ')  # ['Spanish', 'Japanese', 'German', 'English', 'Chinese']

# looping in the list. The basic syntax is:
# [func(ele) for func(ele) in a_list if func(ele)]
# For example:
nations = [language for language in natr_language_new if language.endswith('ese')]
# format number in list to 2 digit
num_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_seq_dd = [format(num, '02d') for num in num_seq]


"""
Lists are versatile Python data structure to group values.
Lists can contain different types, e.g. strings, numbers, 
functions, lists, ...
"""
p = [2, 3, 5, 7, 11]
print(p)  # [2, 3, 5, 7, 11]

# indexing
print(p[0])  # 2
print(p[-1])  # 11

# slicing
print(p[:2])  # [2, 3]
print(p[-3:])  # [5, 7, 11]

# appending
p.append(13)  # [2, 3, 5, 7, 11, 13]
p.extend([17, 19])  # [2, 3, 5, 7, 11, 13, 17, 19]

l = list('hallo')  # ['h', 'a', 'l', 'l', 'o']
l.sort()  # ['a', 'h', 'l', 'l', 'o']

"""
Dictionary: Essentially mapping keys to values
"""

# Creating a dictionary
# GDP per capital (Nominal) 2017
gdp_percap = {'China': 8612,
              'France': 39827,
              'Germany': 12345,  # dummy number
              'Italy': 32038,
              'Japan': 38214,
              'Korea': 29958,
              'Russia': 10846,
              'Turkey': 10498,
              'UK': 39532,
              'USA': 59939}

# Accessing
print(f'{gdp_percap["Germany"]}')  # 44680
# Changing value
gdp_percap['Germany'] = 44680
print(gdp_percap)

# Getting keys and values
print(gdp_percap.keys())
print(gdp_percap.values())

# Adding more than 1 elements
gdp_percap.update({'Singapore': 56746, 'Spain': 28175})
print(gdp_percap)

# Given a dataset in dict form, operation by the values
# Find min and max values by transforming to zip type
min_value = min(zip(gdp_percap.values(), gdp_percap.keys()))
max_value = max(zip(gdp_percap.values(), gdp_percap.keys()))

print(f'min price: {min_value}')
print(f'max price: {max_value}')

# Sort elements by the values
gdppc_sorted = sorted(zip(gdp_percap.values(), gdp_percap.keys()))
for gdppc, country in gdppc_sorted:
    print(f'{country}: {gdppc}')

# Subset of a dictionary (Slicing dictionary by condition)
gdp_subset = {key: value for key, value in gdp_percap.items() if value >= 30000}


"""
For Loop can iterate over all iterables.
All iterables have a method __iter__ which returns an iterator
"""
l = list([1, 2, 3, 4, 5])
for i in l:
    print(i * 2, end=' ')
# 2 4 6 8 10

for i in range(6):
    if i == 3:
        continue
    print(i * 2, end=' ')
# 0 2 4 8 10

for i in 'DEDA':
    print(i, end=' ')
# D E D A

d = dict(a=1, b=2)
for k, v in d.items():
    print('{} has value {}'.format(k, v))
# a has value 1
# b has value 2


"""
Control Flow Tools: if/elif/else
"""
x = 10
if x < 0:
    print('Negative value')
elif x == 0:
    print('Zero')
else:
    print('Positive value')
# Positive value

# Conditions can be combined or altered with: and, or, not, is, is not
# Comparision statements can be used
p = [2, 3, 5, 7, 11]
print(3 in p)  # True
print(3 in p and 4 in p)  # False
print(3 in p or 4 in p)  # True
if x is not None:
    print('Value x is not None')
# Alternative
if not x is None:
    print('Value x is not None')

"""
While loop
There is no Do-While-Loop
"""
# Fibonacci series: sum of two preceding numbers defines next number

a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, b + a
# 1 1 2 3 5 8 13 21 34 55 89
# ATTENTION: Make sure not to have infinite loop (loop with tautology in condition)

# Do While Loop
fib = [0, 1]
while True:
    fib.append(sum(fib[-2:]))
    if fib[-1] > 100:
        break
print(fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

"""
Function definition
"""


def square_numeric(x):
    """ Squares numeric x"""
    return x ** 2


def square_iterable(x):
    """ Squares numerics in iterable x"""
    ret = []
    for i in x:
        ret.append(square_numeric(i))
    return ret


def square_iterabel_short(x):
    """ Squares numerics in iterable x"""
    return [square_numeric(i) for i in x]


x = [1, 2, 3, 4, 5]
square_iterable(x)  # [1, 4, 9, 16, 25]
square_iterabel_short(x)  # [1, 4, 9, 16, 25]


"""
Wiggling Elephant Trunk

vonNeuman_elephant.py
    "With four parameters I can fit an elephant,
       and with five I can make him wiggle his trunk."

Original Versions:

    Author[1]: Piotr A. Zolnierczuk (zolnierczukp at ornl dot gov)
    Retrieved on 14 September 2011 from
    http://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant/
Modified to wiggle trunk:
    2 October 2011 by David Bailey (http://www.physics.utoronto.ca/~dbailey)

    Author[2]:
    Advanced Physics Laboratory
    https://www.physics.utoronto.ca/~phy326/python/

Based on the paper:
    "Drawing an elephant with four complex parameters", by
    Jurgen Mayer, Khaled Khairy, and Jonathon Howard,
    Am. J. Phys. 78, 648 (2010), DOI:10.1119/1.3254017

    The paper does not specify how the wiggle parameter controls the
    trunk, so a guess was made.

Inspired by John von Neumann's famous quote (above) about overfitting data.
    Attributed to von Neumann by Enrico Fermi, as quoted by
      Freeman Dyson in "A meeting with Enrico Fermi" in
      Nature 427 (22 January 2004) p. 297
      
Python Version: 3.6
Modified based on author[2]'s work
Author: Junjie Hu

Overfiting problem in trading strategy stated:
Bailey, D., Borwein, J., Lopez de Prado, M., & Zhu, Q. (2014).
Pseudo-mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance.

"""

# import matplotlib
# matplotlib.use('TKAgg')
from matplotlib import animation
from numpy import append, cos, linspace, pi, sin, zeros
import matplotlib.pyplot as plt

# elephant parameters
parameters = [50 - 30j, 18 + 8j, 12 - 10j, -14 - 60j, 20 + 20j]


def fourier(t, C):
    f = zeros(t.shape)
    for k in range(len(C)):
        f += C.real[k] * cos(k * t) + C.imag[k] * sin(k * t)
    return f


def elephant(t, p):
    npar = 6

    Cx = zeros((npar,), dtype='complex')
    Cy = zeros((npar,), dtype='complex')

    Cx[1] = p[0].real * 1j
    Cy[1] = p[3].imag + p[0].imag * 1j

    Cx[2] = p[1].real * 1j
    Cy[2] = p[1].imag * 1j

    Cx[3] = p[2].real
    Cy[3] = p[2].imag * 1j

    Cx[5] = p[3].real

    x = append(fourier(t, Cy), [p[4].imag])
    y = -append(fourier(t, Cx), [-p[4].imag])

    return x, y


def init_plot():
    # draw the body of the elephant
    # create trunk
    x, y = elephant(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(0)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,


def move_trunk(i):
    x, y = elephant(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    # move trunk to new position (but don't move eye stored at end or array)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(i)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,


fig, ax = plt.subplots()
# initial the elephant body
x, y = elephant(t=linspace(0.4 + 1.3 * pi, 2.9 * pi, 1000), p=parameters)
plt.plot(x, y, 'b.')
plt.xlim([-75, 90])
plt.ylim([-70, 87])
plt.axis('off')
trunk, = ax.plot([], [], 'b.')  # initialize trunk

ani = animation.FuncAnimation(fig=fig,
                              func=move_trunk,
                              frames=1000,
                              init_func=init_plot,
                              interval=100,
                              blit=False,
                              repeat=True)
plt.show()
