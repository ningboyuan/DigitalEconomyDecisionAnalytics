# **DEDA Unit 2** : Data Structure and Commonly Used Operations

### **List**

"""
Recap: List items are ordered, changeable, and allow duplicate values.
The first item has the index [0].
Using list makes Python code simple. A skilful handling of lists requires a broad knowledge of functions and methods for lists.
"""

languages = ['C++', 'Java', 'C#']
print(languages)
python = ['Python 2.7', 'Python 3.6']
print(python)

print(len(languages))  # counts items of the list. The output is 3.
print(len(languages[1]))  # counts items of the 2nd item of the list. The output is 4.

languages.append('JavaScript')  # adds one element at the end of the list.
print(languages) # The output is ['C++', 'Java', 'C#','JavaScript'].

languages.insert(0, 'Python')  # adds one element at arbitrary place (e.g. 0 for the beginning position)
print(languages) # The output is ['Python', 'C++', 'Java', 'C#','JavaScript'].

languages.extend(python)  # adds multiple elements at the end of the list, i.e., to concatenate language and python defined before.
print(languages) # The output is ['Python', 'C++', 'Java', 'C#', 'JavaScript', 'Python 2.7', 'Python 3.6'].

"""
Some more built-in methods that can be used on lists in Python.
"""

languages.remove('C#') # removes specific element from list
print(languages) # The output is ['Python', 'C++', 'Java', 'JavaScript', 'Python 2.7', 'Python 3.6'].

languages.pop(-1)  # removes the last element of the list …
print(languages) # The output is ['Python', 'C++', 'Java', 'JavaScript', 'Python 2.7'].

del languages[-1] # … and this does so too.
print(languages) # The output is ['Python', 'C++', 'Java', 'JavaScript'].

languages_str = '; '.join(languages)  # converts list variable to string variable, adding '; ' to separate the elements of string variable.
print(languages_str) # The output is Python; C++; Java; JavaScript.

languages_new = languages_str.split('; ')  # converts string variable to list variable, removing the separator '; '.
print(languages_new) # The output is ['Python', 'C++', 'Java', 'JavaScript'].

"""
Some more built-in methods that can be used on lists in Python.
"""

numbers = [4, 11, 2, 95, 0]
print(numbers)

# basic search in list
min_num = min(numbers) # finds the minimum value.
print(min_num) # The output is 0.
max_num = max(numbers) # finds the maximum value.
print(max_num) # The output is 95.
sum_num = sum(numbers) # calculates the sum of all elements.
print(sum_num) # The output is 112.
index_num = numbers.index(11) # locates the element 11.
print(index_num) # The output is 1.

# reorder list
numbers.reverse() # reverses the list.
print(numbers) # The output is [0, 95, 2, 11, 4].
numbers.sort() # sorts all elements ascendingly.
print(numbers) # The output is [0, 2, 4, 11, 95].
numbers.sort(reverse=True) # sorts all elements descendingly.
print(numbers) # The output is [95, 11, 4, 2, 0].
sorted_number = sorted(numbers) # uses sorted() function to sort all elements descendingly.
print(sorted_number) # The output is [0, 2, 4, 11, 95].

# formatting numbers of list to 2 digits
numbers_db = [format(num, '02d') for num in numbers] # '02d' denotes for 2 digits.
print(numbers_db) # The output is ['95', '11', '04', '02', '00'].

### **Tuple**

"""
A tuple is an ordered and immutable sequence of Python objects. A tuple is explicitly created by () and its items are separated by commas. Implicit creation of a tuple happens when we set up multiple variables at one line. This is known as tuple packing.
"""

t = () # empty tuple
t1, t2, t3 = 'Guido van Rossum', 65, 'Dutch' # tuple is implicitly created

# tuple vs. list
creator_tuple = ('Guido van Rossum', 65, 'Dutch')
print(creator_tuple) # () represents tuple
creator_list = ['Guido van Rossum', 65, 'Dutch']
print(creator_list) # [] represents list

# accessing tuples works like accessing lists, however …
# … tuple do not support item assignment while lists do
creator_tuple[0] = 'G.v. Rossum' # TypeError! Python stops.
print(creator_tuple)

creator_list[0] = 'G.v. Rossum' # The output is ['G.v. Rossum', 65, 'Dutch'].
print(creator_list)

### **Set and Frozenset**

"""
Python also provides two set types, set and frozenset. A Set is an unordered collection data type that is iterable and has no duplicate items. While the set type is mutable, frozenset is not. 
"""

first_set = set()  # empty set
second_set = {1,2,3} # also a set
not_a_set = {} # empty dict; can use type() function to check the type of it.

first_frozenset = frozenset()  # empty frozenset, cannot be changed anymore.
second_frozenset = ({1,2,3}) # also a frozenset with {}
third_frozenset = ([4,5,6]) # again: a frozenset with []

# define the following four sets to be used
ordered_mutable = {'list', 'list'} # {} sets will drop duplicated elements automatically
print(ordered_mutable)
ordered_immutable = {'string', 'tuple'}
unordered_immutable = {'dictionary', 'frozenset'}
unordered_mutable = {'set'}

# merge 2 sets into 1 w/o duplicates
ordered = ordered_mutable.union(ordered_immutable) # {'string', 'tuple'} + {'list'}
print(ordered) # The output is {'string', 'tuple', 'list'}.

"""
The common set of arithmetic operators are available as methods for sets. 
"""

immutable = ordered_immutable.union(unordered_immutable) # the union set
print(immutable) # The output is {'string', 'tuple', 'frozenset', 'dictionary'}.

inter = immutable.intersection(ordered) # the intersection set
print(inter) # The output is {'string', 'tuple'}.

diff1 = immutable.difference(ordered)  # the difference set (former - later)
print(diff1) # The output is {'frozenset', 'dictionary'}.
diff2 = ordered.difference(immutable)  # the difference set (former - later)
print(diff2) # The output is {'list'}.

sym = ordered.symmetric_difference(immutable)  # all elements that in one set but not in the other set, i.e. diff1 + diff2
print(sym) # The output is {'frozenset', 'dictionary', 'list'}.

disj = ordered.isdisjoint(immutable)  # check if two sets are disjoint.
print(disj) # The output is False.

### **Dict**

"""
Recap: A dictionary, dict type, is formed by 2 parts, a unique key and values.
"""

profile = {'name': 'Guido von Rossum', 'birth': '31-01-1956', 'gender': 'male', 'height': 1.73}
print(profile)
print(profile['name'])  # finds the value by using the key (key:value pair); The output isGuido von Rossum.

keys = list(profile.keys()) # uses keys() to get all the keys and put into a list (key:value pair)
print(keys) # The output is ['name', 'birth', 'gender', ‘height'].
values = list(profile.values())  # uses values() to get all values and put into a list (key:value pair)
print(values) # The output is ['Guido von Rossum', '31-01-1956, 'male', 1.73].

key_value = list(profile.items()) # uses items() to get all key:value pairs; subsequently put them into a list
print(key_value) # The output is the []-list [('name', 'Guido von Rossum'), ('birth', '31-01-1956'), ('gender', 'male'), ('height', 1.73)].

profile['net worth'] = 10000000 # adds a key:value pair; ['net worth': 10000000]
print(profile)

profile['name'] = 'G.v.Rossum' # changes the value of a key
print(profile)

profile.update({'height': '5ft 8', 'nationality': 'Dutch'}) # uses update() to alter multiple (more than) keys & values
print(profile)

### **Conditional Execution**

"""
Conditional programming, or branching, is about evaluating conditions: if …, then …  The operator "is" is used to evaluate if two 2 variables pointed to the same object, "==" is used to evaluate the equivalence of 2 variables.
"""

seq1 = [True, False, 0, 1, -1, 100, '', (), [], {}, [False], [True]]
seq2 = [True, False, 0, 1, -1, 100, '', (), [], {}, [False], [True]]

print(seq1 == seq2)  # The output is True
print(seq1 is seq2)  # The output is False

seq3 = seq2 # reassigning
print(seq3 == seq2)  # The output is True
print(seq3 is seq2)  # The output is True

# False, 0, empty sequence will be evaluated as False
for item in seq1:
    if item: # if item is True; bool-type variable (which returns only True or False)
        print(item, ": This is True")
    elif not item: # if item is False
        print(item, ": This is False")
# The output is:
#    True : This is True
#    False : This is False
#    0 : This is False
#    1 : This is True
#    -1 : This is True
#    100 : This is True
#     : This is False
#    () : This is False
#    [] : This is False
#    {} : This is False

# The following loop gives the same output.
for item in seq1:
    if item == True:
        print(item, ": This is True")
    else:
        print(item, ": This is False")

### **Iteration**

"""
An iterable is an object that can be iterated upon, meaning that it can return its times one by one. Example of iterables include all sequence types (i.e. lists, str, tuple) and some non-sequence types, such as dict. The for loop automatically creates a temporary variable to hold the iteration for the duration of the loop.
"""

repos = ['Introduction', 'ConditionIteration', 'WebScrapingIntro']
units = ['Unit1', 'Unit2', 'Unit3']

for i in range(len(repos)): # algorithm (1): inefficient and not pythonic!
    repo = repos[i] # i iterates over the positions (0,1,2) in list repos
    unit = units[i] # i iterates over the positions (0,1,2) in list units
    print(unit, repo)

for idx, repo in enumerate(repos): # algorithm (2): better, still not beautiful! enumerate() function adds a counter to an iterable and returns it in a form of enumerating object, often used in for loop
    unit = units[idx]
    print(unit, repo)

for unit, repo in zip(units, repos): # algorithm (3): beautiful Python code! zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
   print(unit, repo)

for unit, repo in zip(units, repos): # (4) even more elegant code!
   print(f'{unit}: {repo}') # f-string

"""
Looping in a list follows a basic syntax: func(ele) for func(ele) in a_list if func(ele)
"""

# example 1
intros = [intro + ' Chapter' for intro in repos if intro.startswith('Intro') or intro.endswith('Intro')]
# startswith()/endswith() function checks whether a given sentence starts/ends with some particular string
print(intros) # The output is ['Introduction Chapter', 'WebScrapingIntro Chapter'].

# The above example is exactly the same as:
a =[a +' Chapter' for a in repos if a.startswith('Intro') or a.endswith('Intro')]
print(a)

# example 2
for repo, unit, intro in zip(repos, units, intros): # recall the zip() function
    if repo + ' Chapter' != intro: # compare results of print(repos) and print(intros) for each index 1,2,3
        print(f'{unit} is not of introductory nature.')
        break # stops whole loop
    elif repo + ' Chapter' == intro:
        continue # rejects all remaining statements and continues with next iteration
    else:
        print('Something went wrong.')

"""
Special Loops
"""

our_class = ['Digital', 'Economy', 'and', 'Decision', 'Analytics']
# a loop embedded in another loop
for word in our_class:
    if word == 'in':
        break
    else:
        for letter in word:
            if letter.isupper() is True: # isupper() function checks whether a letter is capital
                print(letter)


# infinite loop
num = 0
while True: # which is always True
    print(num)
    num +=1 # better not run it

### **Import Packages**


"""
# Python provides us with four different way of importing modules of an external package. Make sure to have the package pre-installed with pip install <module>.
"""

# (1) import <module_name>
# for the import of the whole module
import numpy

# (2) import <module_name> as <self-chosen_name>
# for the import of the whole module with an alias
import numpy as np

# (3) from <module_name> import <name(s)>
# for the import of an specific object of the module
from numpy import array
from numpy import * # imports everything from the module numpy

# (4) from <module_name> import <name(s)> as <self-chosen_name>
# for the import of an specific object of the module with an alias
from numpy import array as ay

### **Read & Write Files**

"""
Opening a file in Python is very intuitive: We call the build-in function open(), pass the filename, and specific the read mode 'r' or 'w' the write mode. To rest assure that the close() function will be called at the end, whatever error might occur, we disseminate our code with a try/finally block. readlines() will put content into a list, every line is a string in the list.
"""
import os
os.getcwd() # to see the current path

# try:
    shakespeare = open(os.getcwd() + '/DEDA_ConditionIteration/shakespeare.txt', 'r', encoding='utf-8')
    # 'r' (reads the file after opening it) and 'utf-8' (Unicode Transformation–8-bit) are set by default
    for line in shakespeare.readlines():
        print(line.strip()) # removes leading and trailing whitespaces
        # strip() function returns a copy of the string in which all chars have been stripped from the beginning and the end of the string (default whitespace characters).
# finally:
    shakespeare.close()

# simplified:
# try:
    shakespeare = open(os.getcwd() + '/DEDA_ConditionIteration/shakespeare.txt','r')
    for string in shakespeare: # no need to call readlines() explicitly, it’s the default
        print(string.strip())
# finally:
    shakespeare.close() # closes the opened file.

"""
The context manager is an alternative to wrapping out code into try/finally blocks, while ensuring the secure open and close of a file. We use the syntax "with open() as <self-chosen name>” to load the content. The true beauty of this code lies in the fact that the close() function will be called automatically for us, even in case of errors. 
"""

with open(os.getcwd() + '/DEDA_ConditionIteration/shakespeare.txt','r') as shakespeare:
    for string in shakespeare:
        print(string.strip())
# after this, shakespeare.close() will be called automatically and is redundant

with open(os.getcwd() + '/DEDA_ConditionIteration/shakespeare.txt', 'a' ) as shakespeare: # 'a' means that open() opens a file for appending, creates the file if it does not exist
    shakespeare.write('BY WILLIAM SHAKESPEARE') # write() writes a string to the file.
# BY WILLIAM SHAKESPEARE will be added to last line of the .txt file
with open(os.getcwd() + '/DEDA_ConditionIteration/shakespeare.txt', 'r') as shakespeare:
    for string in shakespeare:
        print(string.strip())

# **Application** : Apple Stocks Data

# **Input and Output**

"""
The Package Pandas supports most of the common structured data formats.
The read_csv method read files as DataFrame type, which is a very powerful data structure that allow us to do almost everything with the data.
"""
import pandas as pd
# AAPL.csv file can be found in GitHub Repository of this Unit or download online from e.g. https://finance.yahoo.com/quote/AAPL/history/

apple_stock = pd.read_csv(os.getcwd() + '/DEDA_ConditionIteration/AAPL.csv', index_col='date', parse_dates=True) # parse_dates: boolean or list of ints or names or list of lists or dict, default False
print(type(apple_stock)) # <class 'pandas.core.frame.DataFrame'>
apple_stock.head() # to see the head of the data set

# Getting the data for year 2021
apple_stock_2021 = apple_stock.loc[apple_stock.index.year == 2021,]
# loc() is used to select rows and columns by number, in the order that they appear in the data frame. It is primarily label based, but may also be used with a boolean array.
# index.year is used to retrieve the data column with the index labelling year.
apple_stock_2021.head() # to see the head of the selected data set

# shape of DataFrame
print(apple_stock_2021.shape)

# sorting by value
apple_stock_2021.sort_values(by='volume', ascending=False, inplace=True) # sort the data by the column 'volume' ascendingly
print(apple_stock_2021)

# check monotonicity increasing through time
print(apple_stock_2021.index.is_monotonic_increasing) # is_monotonic_increasing() function

# sorting by index
apple_stock_2021.sort_index(axis=0, ascending=True, inplace=True) # axis=0 or axis='index' means sort by index, axis=1 or axis='columns' means sort by columns.
print(apple_stock_2021.sort_index)

# reset index as numeric
# reset_index() resets the index of the DataFrame, and uses the default one instead.
apple_stock_2021.reset_index(drop=False, inplace=True) # inplace=True means operation in-place.
# If set drop = True , reset_index() will delete the index instead of inserting it back into the columns of the DataFrame. If set drop = True , the current index will be deleted entirely and the numeric index will replace it
print(apple_stock_2021.reset_index)

# check null values
nan_rows = apple_stock_2021[apple_stock_2021['open'].isna()] # isna() function for the column 'open'
print(nan_rows)

# remove null values
apple_stock_2021.dropna(axis=0, how='any', subset=['volume', 'close'], inplace=True) # dropna() function for the columns 'volume' and 'close'
# how='any': If any NA values are present, drop that row or column
# how='all': If all values are NA, drop that row or column.

# set a column as index
apple_stock_2021.set_index(keys='date', drop=True, append=False, inplace=True) # the column 'date' is chosen as the index, keys means the label or array-like or list of labels/arrays

# duplicates timestamp operations
print(apple_stock_2021.index.has_duplicates) # index.has_duplicates() function returns to True or False
apple_stock_2021.index.duplicated() # index.duplicated() indicates duplicate index values

# drop_duplicates() returns DataFrame with duplicate rows removed
data = pd.DataFrame({'A':[1,1,2,2],'B':['a','b','a','b']})
data.drop_duplicates('B','first',inplace=True)
print(data)

# operation:
# way1 to drop the duplicate data, which induces potential risk
way1 = apple_stock_2021.drop_duplicates(keep='first', subset=['low', 'high', 'open', 'close', 'volume'])
print(way1)

# way2, dropping duplicate data by index for the row by using the operation ~, which takes the (bit-wise) inverse of an array (element-wise)
way2 = apple_stock_2021[~ (apple_stock_2021.index.duplicated())]
print(way2)

# a simple build-in plot function of pandas
apple_stock_2021['open'].plot()
apple_stock_2021['close'].plot()
import matplotlib.pyplot as plt

# Save the new data as json format
plt.savefig(os.getcwd() + '/DEDA_ConditionIteration/apple_stock_2021.png',dpi=500)
plt.show()
apple_stock_2021.to_json('AAPL_2021.json')
