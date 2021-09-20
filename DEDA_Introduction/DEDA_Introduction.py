"""
Python Basic Syntax and Data Structure Introduction

Author: Junjie Hu
Editor: Lucas Uman and Isabell Fetzer

"""

"""
numeric
"""
"""  
This is a multi-line comment block. It is set in-between six quotation marks.
Python provides a straight way for numerical operations.
Try the basics:
+, -, *, /, %, **, // 
"""

# This is a one-line comment in Python. It extends to the end of the physical line.

a = 5  # initiates integer variable a which the value 5 is assigned to
b = 3  # another integer variable b which the value 3 is assigned to
b = 5  # the old value of b is overwritten by 5

a, b = 7, 3  # initialising two variables at once: a takes the value  7; b takes 3

a += 1  # short for a = a+1 so again a new value is assigned to a

"""
functions
"""
"""  
Python provides versatile set of functions for variables.
"""

print(a)  # the fct. print() prints out the value of a; the output is 8
c = round(a / b)  # the fct. round() rounds 8/3 and assigns the output to c

# Function can also take arguments, which allow us further specifications.

c = round(a / b, ndigits=4)  # ndigits specifies the number of decimal places
print(c)  # output is 2.6667
c = round(a / b, 3)  # arguments do not need to be spelled out, if placed correctly
print(c)  # output is 2.667

"""
string
"""
""" 
String is a basic type in python, it's commonly used and very powerful.
"""

w = 'Hello'  # initiates string variables by single quotation marks
x = "World"  # … or by double quotation marks
print(w + x)  # HelloWorld

y = '20'  # numbers can also be assigned as strings too
e = '10'
print(y + e)  # concatenates strings so output is ‘2010’

f = int(y) + int(e)  # the fct. int() converts strings to integers, f is 30 now

# formatting strings
# using f '….'  string, you can write variable names inside the brackets {}, directly.
greeting = f'{w} Python-{x}.'  # Hello Python-World.
greeting = f'{w} {x.upper()}.'  # Hello WORLD.

"""
comparison
"""
"""
Python provides a straight way for numerical operations. Try comparison operations ==,<,<=,>,>=,!=
"""

a = 5

a == 5  # checks if a equals 5; output will be True
a != 7  # checks if a is not equal to 7; output will be True

a <= 7  # checks if a is smaller or equal 7; output will be True
a > 5  # False

a = 'A'  # old integer value of a (which is 7) is overwritten by string value ‘A’
b = 'B'  # old integer value of b (which is 3) is overwritten by string value ‘B’
a == b  # False
a != b  # True

"""
list
"""
"""
List is a versatile Python data type to group values.
In Python a list is created by placing all the items inside square brackets [] , separated by commas.
"""
my_list = []  # initiates an empty list, which we choose to call “my_list”
my_list = [2, 3, 5, 7, 11]  # adds elements to the list
print(my_list)  # output: [2, 3, 5, 7, 11]

# indexing
my_list[0]  # the first element of my_list is called, which is 2
my_list[-1]  # the last element of my_list is called, which is 11

# slicing
my_list[:2]  # calls the first two elements of my_list [2, 3]
my_list[-3:]  # calls the last three elements [5, 7, 11]

# appending
my_list.append(13)  # [2, 3, 5, 7, 11, 13]
my_list.extend([17, 19])  # [2, 3, 5, 7, 11, 13, 17, 19]

"""
list
"""
"""
Lists can contain different types, e.g. strings, numbers, 
functions, lists, …
"""

my_list = ['Welcome', 'to', 'Python']  # adds three string elements to the list
print(my_list[0])  # Welcome
print(my_list[1])  # to

print(my_list)  # [‘Welcome', 'to', ‘Python']

# using for loop to iterate all elements in the list:
for word in my_list:  # word we choose randomly, any other name works too
    print(word)

# the output is:
# Welcome
# to
# Python


"""
list
"""
"""
Functions can help when working with lists.
"""

# to print it out in one line we need to apply the fct join() to our list:
list_as_sentence = '*'.join(my_list)  # sets * as separators
print(list_as_sentence)  # Welcome*to*Python

list_as_sentence = ' '.join(my_list)  # sets white spaces as separators
print(list_as_sentence)  # Welcome to Python

# Try to execute this code and see what happens.
list_sliced = list_as_sentence[0:12]  # slices string by indices
print(f'{list_sliced}.')  # Welcome to P.

# Try changing the indices to negative.

sentence_big = list_as_sentence.upper()
print(sentence_big)  # WELCOME TO PYTHON

"""
operations
"""
"""
Checking for possible operations: 
"""

# by using dir() function, or help() function; you may see all ops on the str object
dir(str)

# or a str instance
dir(sentence_big)

# likewise,
help(str)

"""
dictionary
"""
"""
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates. 
"""
course = dict(name='DEDA', unit=0)  # {'name': 'DEDA', 'unit': 0}
course = {'name': 'DEDA', 'unit': 0}  # alternative

# accessing
course['unit']  # 0

# assigning
course['unit'] = 1

# get keys
course.keys()  # ['name', 'unit']
course.values()  # ['DEDA', 1]

# adding values
course.update({'lecturers': ['Chen', 'Härdle']})
# {'lecturers': ['Chen', 'Härdle'], 'name': 'DEDA', 'unit': 1}


"""
if
"""
"""
Control Flow Tools: if/elif/else. 
Comparison statements can be used. 
"""

x = 10  # initialising a numeric variable x

if x < 0:  # checking for the value of x
    print('Negative Value')  # note the four additional level of indentation (4 spaces)
elif x == 0:
    print('Zero')
else:
    print('Positive Value')

"""
if
"""
"""
Control Flow Tools: if/elif/else
"""

# Conditions can be combined or altered with: and, or, not, is, is not
p = [2, 3, 5, 7, 11]  # initialising a list p
3 in p  # True
3 in p and 4 in p  # False
3 in p or 4 in p  # True

# Empty/Missing Values can be initialised by the term “None”
y = None  # initialising an empty variable x

if y is not None:  # alternatively: if not y is None: ….
    print('Value is not None')
else:
    print('Value is None')

"""
for loop
"""
"""
For Loop can iterate over all elements. The i is a self-chosen variable to use to represent the current increment in a loop. 
"""
l = list([1, 2, 3, 4, 5])
for i in l:
    print(i * 2, end=' ')  # output: 2 4 6 8 10

for i in range(6):  # iterates from 0 to 5
    if i == 3:
        continue  # skip 3*2 in output
    print(i * 2, end=' ')  # output:  0 2 4 8 10

for i in 'DEDA':
    print(i, end=' ')  # output: D E D A

d = dict(a=1, b=2)
for k, v in d.items():
    print('{} has value {}'.format(k, v))
# a has value 1
# b has value 2


"""
while loop
"""
"""
With the while loop we can execute a set of statements as long as a condition is true. ATTENTION: Make sure not to have infinite loop (loop with tautology in condition).
"""

# Fibonacci series: sum of two preceding numbers defines next number
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, b + a
# 1 1 2 3 5 8 13 21 34 55 89


"""
while loop
"""
"""
The < break > statement in Python terminates the current loop and resumes execution at the next statement.
"""

fib = [0, 1]  # a list called fib
while True:
    # appends the sum of the last 2 elements of our list to our new list
    fib.append(sum(fib[-2:]))
    if fib[-1] > 100:
        break
print(fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

"""
function
"""
"""
Define your own function using def, followed by a name, parameters in parentheses (), a colon, and a block of code.
"""


def my_first_fct():
    print('This is my first function.')  # remember the four indentation


my_first_fct()  # call the function


# another function with two parameter m and n
def my_second_fct(m, n):
    mn = m % n
    return print(f'The remainder of the devision of {m} by {n} is {mn}.')


my_second_fct(4, 3)  # call the function and pass the variables m = 4 and n = 3
my_second_fct(7, 2)  # call the function again and pass other variables

"""
function
"""
"""
Another example for functions
"""


def square_numeric(x):  # Squares numeric x
    return x ** 2


def square_iterable(x):  # Squares numerics in iterable x
    list = []
    for i in x:
        list.append(square_numeric(i))
    return list


def square_iterabel_short(x):  # Squares numerics in iterable x
    return [square_numeric(i) for i in x]


x = [1, 2, 3, 4, 5]
square_iterable(x)  # [1, 4, 9, 16, 25]
square_iterabel_short(x)  # [1, 4, 9, 16, 25]


"""
Wiggling Elephant Trunk:

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
from IPython.display import HTML

# PLEASE NOTE IN SPYDER YOU SHOULD DISABLE THE ACTIVE SUPPORT in PREFs
# elephant parameters
parameters = [50 - 30j, 18 + 8j, 12 - 10j, -14 - 60j, 20 + 20j]

# patrick's happy spermwhale
# parameters = [30 - 10j, 20 + 20j, 40 + 10j, 20 - 50j, -40 + 10j]

# philipp's flying swan 
# parameters = [1 - 2j, 9 + 9j, 1 - 2j, 9 + 9j, 0 + 0j]

# kathrin's hungry animal 
# parameters = [50 - 50j, 30 + 10j, 5 - 2j, -5 - 6j, 20 + 20j]

# anna’s happy hippo
# parameters = [50 - 15j, 5 + 2j, -10 - 10j, -14 - 60j, 5 + 30j]

# fabio’s bird with right wing paralysis
# parameters = [50 - 15j, 5 + 2j, -1 - 5j, -14 - 60j, 18 - 40j]

# for pea shooter see code below 

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

    x = append(fourier(t, Cy), [p[4].real])
    y = -append(fourier(t, Cx), [-p[4].imag])

    return x, y


def init_plot():
    # draw the body of the elephant & create trunk
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

ani
HTML(ani.to_html5_video())

""" 
# Uncomment if you would like to save video externally
Writer = animation.writers['ffmpeg']
metadata = dict(title='Elephant Trunk Wiggling', artist='Jenny Bethäuser')
writer = Writer(fps=30, metadata=metadata, bitrate=1800)
ani.save(filename='bulldog_trunk_wiggle.mp4', writer=writer)
plt.show()
"""


"""
Wentian’s pea shooter:

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

# for peashooter: 

# import matplotlib
# matplotlib.use('TKAgg')
"""
you might want to use the following in terminal if the graphviz does not work:
conda install -c conda-forge ffmpeg
All should be fine though if you use jupyter notebook
"""

from matplotlib import animation
from numpy import append, cos, linspace, pi, sin, zeros
import matplotlib.pyplot as plt


parameters = [50 - 50j, 18 + 80j, 12 - 10j, -14 - 60j, 20 + 20j]


def fourier(t, C):
    f = zeros(t.shape)
    for k in range(len(C)):
        f += C.real[k] * cos(k * t) + C.imag[k] * sin(k * t)
    return f


def peashooter(t, p):
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

    x = append(fourier(t, Cy), [p[4].real])
    y = -append(fourier(t, Cx), [-p[4].imag])

    return x, y


def init_plot():
    x, y = peashooter(linspace(2 * pi + 0.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(0)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,


def move_trunk(i):
    x, y = peashooter(linspace(2 * pi + 0.8 * pi, 0.4 + 3.7 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(i)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,


fig, ax = plt.subplots()
x, y = peashooter(t=linspace(0.4 + 1.7 * pi, 2 * pi + 0.8 * pi, 1000), p=parameters)
plt.plot(x, y, 'b.')
plt.xlim([-175, 190])
plt.ylim([-70, 100])
plt.axis('off')
trunk, = ax.plot([], [], 'b.') 

ani = animation.FuncAnimation(fig=fig,
                              func=move_trunk,
                              frames=1000,
                              init_func=init_plot,
                              interval=500,
                              blit=False,
                              repeat=True)


# Video will be externally saved
Writer = animation.writers['ffmpeg']
metadata = dict(title='Wentians pea shooter')
writer = Writer(fps=30, metadata=metadata, bitrate=1800)
ani.save(filename='peashooter.mp4', writer=writer)
# plt.show()

