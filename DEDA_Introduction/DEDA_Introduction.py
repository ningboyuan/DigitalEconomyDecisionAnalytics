### **Python Basic Syntax and Data Structure Introduction**

### **Numerics**
"""
This is a multi-line comment block. It is set in-between six quotation marks.
Python provides a straight way for numerical operations.
Try the basics:
+, -, *, /, %, **, //
"""
# This is a one-line comment in Python. It extends to the end of the physical line.

a = 5  # initiates integer variable a which the value 5 is assigned to
print(a)
b = 3  # initiates another integer variable b which the value 3 is assigned to
print(b)
b = 5  # overwrites the old value of b by 5
print(b)
a, b = 7, 3  # initiate two variables at once: a takes the value 7; b takes 3
print(a, b)
a += 1  # is a simplified version for a = a+1 so again a new value is assigned to a
print(a)
a -= 1  # is a simplified version for a = a-1 so again a new value is assigned to a
print(a)

### **Functions**
"""  
Python provides versatile set of functions for variables.
"""

print(a)  # the function print() prints out the value of a; the output is 8
print(b)
c = round(a / b)  # the function round() rounds 8/3 and assigns the output to c
print(c)
# Function can also take arguments, which allow us for further specifications.
c = round(a / b, ndigits=4)  # ndigits specifies the number of decimal places
print(c)  # output is 2.6667
c = round(a / b, 3)  # arguments do not need to be spelled out, if placed correctly
print(c)  # output is 2.667

## **Strings**
""" 
String is a basic type in python, it's commonly used and very powerful.
"""

w = 'Hello'  # initiates string variables by single quotation marks
x = "World"  # … or by double quotation marks
print(w + x)  # output is HelloWorld

y = '20'  # numbers can also be assigned as strings too
e = '10'
print(y + e)  # concatenates strings so output is ‘2010’

f = int(y) + int(e)  # the function int() converts strings to integers, f is 30 now
print(f)

# formatting strings
# using f '….'  string, you can write variable names inside the brackets {}, directly.
greeting = f'{w} Python-{x}.'
print(greeting)  # output is Hello Python-World.
greeting = f'{w} {x.upper()}.'  # the function .upper() capitalizes letters in string
print(greeting)  # output is Hello WORLD.

### **Comparison**
"""
Python provides a straight way for numerical operations. Try comparison operations ==,<,<=,>,>=,!=
"""

a = 5
print(a == 5)  # checks if a equals 5; output will be True
print(a != 7)  # checks if a is not equal to 7; output will be False

print(a <= 7)  # checks if a is smaller than or equal to 7; output will be True
print(a > 5)  # checks if a is greater than 5; output will be False

a = 'A'  # overwrites the old integer value of a (which is 7) by a string value ‘A’
b = 'B'  # overwrites the old integer value of b (which is 3) by a string value ‘B’
print(a == b)  # Comparison of string a and string b; False
print(a != b)  # Comparison of string a and string b; True

### **Lists**

"""
List is a versatile Python data type to group values.
In Python a list is created by placing all the items inside square brackets [] , separated by commas.
"""

my_list = []  # initiates an empty list, which we name as “my_list”
my_list = [2, 3, 5, 7, 11]  # adds five elements to the list
print(my_list)  # output: [2, 3, 5, 7, 11]

# indexing
print(my_list[0])  # the first element of my_list is called, which is 2
print(my_list[-1])  # the last element of my_list is called, which is 11

# slicing
print(my_list[:2])  # calls the first two elements of my_list; the output is [2,3]
print(my_list[-3:])  # calls the last three elements of my_list, the output is [5, 7, 11]

# appending
my_list.append(13)  # appends an element to my_list at the end, the output is [2, 3, 5, 7, 11, 13]
print(my_list)
my_list.extend(
    [17, 19])  # appends more than one elements to my_list at the end, the output is [2, 3, 5, 7, 11, 13, 17, 19]
print(my_list)

"""
Lists can contain different types, e.g. strings, numbers, 
functions, lists, …
"""

my_list = ['Welcome', 'to', 'Python']  # adds three string elements to the list
print(my_list[0])  # the output is Welcome
print(my_list[1])  # the output is to
print(my_list)  # the output is [‘Welcome', 'to', ‘Python']

# using for loop to iterate all elements in the list:
for word in my_list:  # word is a randomly chosen index, any other name can work too
    print(word)

"""
Functions can help when working with lists.
"""

# to print it out in one line we need to apply the function join() to our list:
list_as_sentence = '*'.join(my_list)  # substitute every (white) space with * as separators
print(list_as_sentence)  # Welcome*to*Python
list_as_sentence = ' '.join(my_list)  # substitute every * with (white) spaces as separators
print(list_as_sentence)  # Welcome to Python

# Try to execute this code and see what happens.
list_sliced = list_as_sentence[
              0:12]  # slices string by indices - the first 12 elements in the string (including white spaces)
print(f'{list_sliced}.')  # the output is Welcome to P.

# Try changing the indices to negative.
sentence_big = list_as_sentence.upper()
print(sentence_big)  # the output is WELCOME TO PYTHON

### **Operations**
"""
Checking for possible operations: 
"""

# by using dir() function, or help() function; you may see all ops on the str object
dir(str)  # returns list of the attributes and methods of any object

# or a str instance
dir(sentence_big)

# likewise,
help(str)

### **Dictionaries**
"""
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is unordered, changeable and does not allow for duplicates.
"""

course = dict(name='DEDA', unit=0)
print(course)  # the output is {'name': 'DEDA', 'unit': 0}
course = {'name': 'DEDA', 'unit': 0}  # an alternative for the same purpose
print(course)

# accessing
print(course['unit'])  # the output is 0

# assigning
course['unit'] = 1  # assign 'unit' with value 1
print(course['unit'])

# get keys
print(course.keys())  # the function keys() returns to the keys of the key:value pair, the output is ['name', 'unit']
print(
    course.values())  # the function keys() returns to the values of the key:value pair, the output is ['name', 'unit']

# adding values
course.update({'lecturers': ['Chen', 'Härdle']})  # the function update() helps appending new key-value pairs
print(course)  # output is {'name': 'DEDA', 'unit': 1, 'lecturers': ['Chen', 'Härdle']}

### **If/elif/else**

"""
Control Flow Tools: if/elif/else. 
Comparison statements can be used. 
"""

x = 10  # initiates a numeric variable x

if x < 0:  # if-statement checking for the value of x
    print('Negative Value')  # note the four additional level of indentation (4 spaces)
elif x == 0:
    print('Zero')
else:
    print('Positive Value')

"""
Control Flow Tools: if/elif/else
"""

# Conditions can be combined or altered with: and, or, not, is, is not
p = [2, 3, 5, 7, 11]  # initiates a list p
print(p)
print(3 in p)  # checks if a element 3 exists in p; True
print(3 in p and 4 in p)  # checks if both elements 3 and 4 exist in p; False
print(3 in p or 4 in p)  # checks if either element 3 or element 4 exists in p; True

# Empty/Missing Values can be also initiated by the term “None”.
y = None  # initiates an empty variable y.

if y is not None:  # alternatively: if not y is None: ….
    print('Value is not None')
else:
    print('Value is None')

### **For loop**

"""
For Loop can iterate over all elements. The i is a self-chosen variable to use to represent the current increment in a loop. 
"""

l = list([1, 2, 3, 4, 5])
for i in l:
    print(i * 2, end=' ')  # the output is: 2 4 6 8 10

for i in range(6):  # range(6) iterates from 0 to 5 (6 natural numbers in total)
    if i == 3:
        continue  # skip 3*2 in output
    print(i * 2, end=' ')  # the output is (1*2 2*2 4*2 5*2): 0 2 4 8 10

for i in 'DEDA':  # i can also be substituted by other variables
    print(i, end=' ')  # output: D E D A

# "{} {}".format("hello", "world"); format() function
# "{1} {0} {1}".format("hello", "world"); format() function specifying positions

d = dict(a=1, b=2)  # alternatively, d = {'a': 1, 'b': 2}
for k, v in d.items():  # items() is a function used to return the list with all dictionary keys with values.
    print('\n{} has value {}'.format(k, v))  # \n is used to insert a newline in the text at this point.
# the output (1st line) is: a has value 1
# the output (2nd line) is: b has value 2

### **While eloop**

"""
# With the while loop we can execute a set of statements as long as a condition is true. ATTENTION: Make sure not to have infinite loop (loop with tautology in condition).
"""

# Fibonacci series: sum of two preceding numbers defines next number
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, b + a  # a is overwritten by b, b is overwritten by b+a
# 1 1 2 3 5 8 13 21 34 55 89

"""
The < break > statement in Python terminates the current loop and resumes execution at the next statement.
"""

# Fibonacci series
fib = [0, 1]  # initiates a list called fib
while True:  # is always Ture - if no break the loop will be infinite
    fib.append(sum(fib[-2:]))  # adds the sum of last two elements of the list fib to the fib's last version
    if fib[-1] > 100:
        break
print(fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

### **Functions**

"""
Define our own functions using def, followed by a name, parameters in parentheses (), a colon, and a block of code.
"""


def my_first_fct():
    print('This is my first function.')  # always note that there should be four indentations


my_first_fct()  # call the function


# another function with two parameter m and n
def my_second_fct(m, n):
    mn = m % n  # division algorithm, m the nominator, n the denominator
    return print(f'The remainder of the division of {m} by {n} is {mn}.')


my_second_fct(4, 3)  # call the function and pass the variables m = 4 and n = 3
my_second_fct(7, 2)  # call the function and pass the variables m = 7 and n = 2

"""
Another example for functions
"""


def square_numeric(x):  # squares numeric x
    return x ** 2  # e.g. 4 power 2 is 16


def square_iterable(x):  # squares numerics in iterable x
    list = []
    for i in x:
        list.append(square_numeric(i))
    return list


def square_iterable_short(x):  # squares numerics in iterable x
    return [square_numeric(i) for i in x]


x = [1, 2, 3, 4, 5]
square_iterable(x)  # the output is [1, 4, 9, 16, 25]
square_iterable_short(x)  # the output is [1, 4, 9, 16, 25]

# **Application 1: Wiggling Elephant Trunk**

"""
Wiggling Elephant Trunk: 

vonNeuman_elephant.py "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk."

Original Versions:

Author[1]: Piotr A.Zolnierczuk(zolnierczukp at ornl dot gov) Retrieved on 14 September 2011 from http://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant /

Modified to wiggle trunk: 2 October 2011 by David Bailey(http://www.physics.utoronto.ca/~dbailey) 

Author[2]: Advanced Physics Laboratory https://www.physics.utoronto.ca/~phy326/python/Based on the paper:

"Drawing an elephant with four complex parameters", by Jurgen Mayer, Khaled Khairy, and Jonathon Howard, Am.J.Phys. 78, 648(2010), DOI: 10.1119 / 1.3254017

The paper does not specify how the wiggle parameter controls the trunk, so a guess was made.

Inspired by John von Neumann's famous quote (above) about overfitting data.

Attributed to von Neumann by Enrico Fermi, as quoted by Freeman Dyson in "A meeting with Enrico Fermi" in Nature 427(22 January 2004) p.297

Python Version: 3.6

Modified based on author[2]'s work

Author: Junjie Hu

Overfiting problem in trading strategy stated:Bailey, D., Borwein, J., Lopez de Prado, M., & Zhu, Q.(2014).

Pseudo - mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance.

"""

import matplotlib  # import the module matplotlib

matplotlib.use('TKAgg')  # open individual windows when plots are shown
from matplotlib import animation  # import the function animation embedded in matplotlib for a wiggling trunk
from numpy import append, cos, linspace, pi, sin, \
    zeros  # import some functions embedded in numpy in order to build up the Fourier coordinate expansions
import matplotlib.pyplot as plt  # import matplotlib.pyplot (name it as plt) for the purpose of plotting
from IPython.display import HTML  # import the function HTML embedded in IPython.display for playing animiations

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

# Fourier coordinate expansion
def fourier(t,
            C):  # t denotes the collection of observation points that should be better spaced evenly (for convenience); C denotes Fourier coefficients to be specified
    f = zeros(
        t.shape)  # shape() returns the size of an object; zeros() returns a new array of given shape and type, filled with zeros.
    # f's initial value is given by 0
    for k in range(len(C)):  # len() denotes the length of C
        f += C.real[k] * cos(k * t) + C.imag[k] * sin(
            k * t)  # real[] and img[] denote the real, imaginary parts of C[k], respectively
    return f


# elephant function
def elephant(t,
             p):  # t denotes the collection of observation points; p denotes the parameters used for specifying C (Fourier coefficients)
    npar = 6

    Cx = zeros((npar,),
               dtype='complex')  # Cx with initial value 0 should be an array containing npar=6 complex vectors, that is, Cx = array([0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])
    Cy = zeros((npar,),
               dtype='complex')  # Cy with initial value 0 should be an array containing npar=6 complex vectors, that is, Cx = array([0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j])

    Cy[1] = p[0].real * 1j
    Cx[1] = p[3].imag + p[0].imag * 1j
    Cy[2] = p[1].real * 1j
    Cx[2] = p[1].imag * 1j
    Cy[3] = p[2].real
    Cx[3] = p[2].imag * 1j
    Cy[5] = p[3].real

    x = append(fourier(t, Cx), [p[4].real])  # add a point as the elephant's eye
    y = append(fourier(t, Cy), [-p[4].imag])  # add a point as the elephant's eye

    return x, -y


# Draw the elephant's body & Create trunk
def init_plot():
    x, y = elephant(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000),
                    parameters)  # linspace() returns evenly spaced numbers (totally 1000) over a specified interval (2.9 * pi, 0.4 + 3.3 * pi).
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(0)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,


# draw the wiggling trunk
def move_trunk(i):
    x, y = elephant(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    # Move the trunk to new position (but don't move eye stored at end or array)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(i)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,


fig, ax = plt.subplots()  # initiates a figure and subplot axes
# initiates the elephant's body
x, y = elephant(t=linspace(0.4 + 1.3 * pi, 2.9 * pi, 1000), p=parameters)
plt.plot(x, y, 'b.')  # 'b.' stands for blue lines
plt.xlim([-75, 90])  # stretches the x-axis to have a better vision
plt.ylim([-70, 87])  # stretches the y-axis to have a better vision
plt.axis('off')  # removes the axes
# Assign the initial value of the elephant's trunk
trunk, = ax.plot([], [], 'b.')

ani = animation.FuncAnimation(fig=fig,  # the figure object used to get needed events, such as draw or resize.
                              func=move_trunk,  # the wiggling trunk function
                              frames=1000,  # the source of data to pass func and each frame of the animation
                              init_func=init_plot,  # the elephant's body and trunk function
                              interval=100,  # the delay between frames in milliseconds.
                              blit=False,  # whether blitting is used to optimize drawing
                              repeat=True)  # whether the animation repeats when the sequence of frames is completed.
ani
HTML(ani.to_html5_video())

# Uncomment if you would like to save video externally
Writer = animation.writers['ffmpeg']
metadata = dict(title='Elephant Trunk Wiggling', artist='Jenny Bethäuser')
writer = Writer(fps=30, metadata=metadata, bitrate=1800)
ani.save(filename='bulldog_trunk_wiggle.mp4', writer=writer)
plt.show()
"""

# **Application 2: Wentian’s Pea Shooter**

"""
"""
Wentian’s pea shooter:
vonNeuman_elephant.py

"With four parameters I can fit an elephant, and with five I can make him wiggle his trunk."

Original Versions:

Author[1]: Piotr A.Zolnierczuk(zolnierczukp at ornl dot gov)
Retrieved on 14 September 2011 from http://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant /

Modified to wiggle trunk:

2 October 2011 by David Bailey(http: // www.physics.utoronto.ca / ~dbailey)
Author[2]: Advanced Physics Laboratory https: // www.physics.utoronto.ca / ~phy326 / python /

Based on the paper:

"Drawing an elephant with four complex parameters", by Jurgen Mayer, Khaled Khairy, and Jonathon Howard, Am.J.Phys. 78, 648(2010), DOI: 10.1119 / 1.3254017
The paper does not specify how the wiggle parameter controls the trunk, so a guess was made.

Inspired by John von Neumann's famous quote (above) about overfitting data.

Attributed to von Neumann by Enrico Fermi, as quoted by Freeman Dyson in "A meeting with Enrico Fermi" in Nature 427(22 January 2004) p.297

Python Version: 3.6

Modified based on author[2]'s work

Author: Junjie Hu

Overfiting problem in trading strategy stated: Bailey, D., Borwein, J., Lopez de Prado, M., & Zhu, Q.(2014).
Pseudo - mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance.
"""

# for peashooter: 

import matplotlib
matplotlib.use('TKAgg')

"""
you might want to use the following in terminal if the graphviz does not work: conda install - c conda - forge ffmpeg 
All should be fine though if you use jupyter notebook
"""

from matplotlib import animation
import matplotlib.animation as animation
from numpy import append, cos, linspace, pi, sin, zeros
import matplotlib.pyplot as plt
from IPython.display import HTML

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
    x, y = peashooter(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(0)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,

def move_trunk(i):
    x, y = peashooter(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(i)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,

fig, ax = plt.subplots()
x, y = peashooter(t=linspace(0.4 + 1.3 * pi, 2.9 * pi, 1000), p=parameters)
plt.plot(x, y, 'b.')

plt.xlim([-175, 190])
plt.ylim([-70, 100])
plt.axis('off')
trunk, = ax.plot([], [], 'b.') 

ani = animation.FuncAnimation(fig=fig,
                              func=move_trunk,
                              frames=1000,
                              init_func=init_plot,
                              interval=100,
                              blit=False,
                              repeat=True)
ani
HTML(ani.to_html5_video())

Writer = animation.writers['ffmpeg']
metadata = dict(title='Wentians pea shooter')
writer = Writer(fps=30, metadata=metadata, bitrate=1800)
ani.save(filename='peashooter.mp4', writer=writer)
plt.show()
