#!/usr/bin/env python
# coding: utf-8

# # Python Quick Reference by [Data School](http://www.dataschool.io/)
# 
# **Related:** [GitHub repository](https://github.com/justmarkham/python-reference) and [blog post](http://www.dataschool.io/python-quick-reference/)
# 
# ## Table of contents
# 
# 1. <a href="#1.-Imports">Imports</a>
# 2. <a href="#2.-Data-Types">Data Types</a>
# 3. <a href="#3.-Math">Math</a>
# 4. <a href="#4.-Comparisons-and-Boolean-Operations">Comparisons and Boolean Operations</a>
# 5. <a href="#5.-Conditional-Statements">Conditional Statements</a>
# 6. <a href="#6.-Lists">Lists</a>
# 7. <a href="#7.-Tuples">Tuples</a>
# 8. <a href="#8.-Strings">Strings</a>
# 9. <a href="#9.-Dictionaries">Dictionaries</a>
# 10. <a href="#10.-Sets">Sets</a>
# 11. <a href="#11.-Defining-Functions">Defining Functions</a>
# 12. <a href="#12.-Anonymous-%28Lambda%29-Functions">Anonymous (Lambda) Functions</a>
# 13. <a href="#13.-For-Loops-and-While-Loops">For Loops and While Loops</a>
# 14. <a href="#14.-Comprehensions">Comprehensions</a>
# 15. <a href="#15.-Map-and-Filter">Map and Filter</a>

# ## 1. Imports

# In[3]:


# 'generic import' of math module
import math
math.sqrt(25)


# In[4]:


# import a function
from math import sqrt
sqrt(25)    # no longer have to reference the module


# In[5]:


# import multiple functions at once
from math import cos, floor


# In[6]:


# import all functions in a module (generally discouraged)
from csv import *


# In[7]:


# define an alias
import datetime as dt


# In[8]:


# show all functions in math module
print(dir(math))


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 2. Data Types
# 
# **Determine the type of an object:**

# In[9]:


type(2)


# In[10]:


type(2.0)


# In[11]:


type('two')


# In[12]:


type(True)


# In[13]:


type(None)


# **Check if an object is of a given type:**

# In[14]:


isinstance(2.0, int)


# In[15]:


isinstance(2.0, (int, float))


# **Convert an object to a given type:**

# In[16]:


float(2)


# In[17]:


int(2.9)


# In[18]:


str(2.9)


# **Zero, `None`, and empty containers are converted to `False`:**

# In[19]:


bool(0)


# In[20]:


bool(None)


# In[21]:


bool('')    # empty string


# In[22]:


bool([])    # empty list


# In[23]:


bool({})    # empty dictionary


# **Non-empty containers and non-zeros are converted to `True`:**

# In[24]:


bool(2)


# In[25]:


bool('two')


# In[26]:


bool([2])


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 3. Math

# In[27]:


10 + 4


# In[28]:


10 - 4


# In[29]:


10 * 4


# In[30]:


10 ** 4    # exponent


# In[31]:


5 % 4      # modulo - computes the remainder


# In[32]:


# Python 2: returns 2 (because both types are 'int')
# Python 3: returns 2.5
10 / 4


# In[33]:


10 / float(4)


# In[34]:


# force '/' in Python 2 to perform 'true division' (unnecessary in Python 3)
from __future__ import division


# In[35]:


10 / 4     # true division


# In[36]:


10 // 4    # floor division


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 4. Comparisons and Boolean Operations

# **Assignment statement:**

# In[37]:


x = 5


# **Comparisons:**

# In[38]:


x > 3


# In[39]:


x >= 3


# In[40]:


x != 3


# In[41]:


x == 5


# **Boolean operations:**

# In[42]:


5 > 3 and 6 > 3


# In[43]:


5 > 3 or 5 < 3


# In[44]:


not False


# In[45]:


False or not False and True     # evaluation order: not, and, or


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 5. Conditional Statements

# In[46]:


# if statement
if x > 0:
    print('positive')


# In[47]:


# if/else statement
if x > 0:
    print('positive')
else:
    print('zero or negative')


# In[48]:


# if/elif/else statement
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')


# In[49]:


# single-line if statement (sometimes discouraged)
if x > 0: print('positive')


# In[50]:


# single-line if/else statement (sometimes discouraged), known as a 'ternary operator'
'positive' if x > 0 else 'zero or negative'


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 6. Lists
# 
# - **List properties:** ordered, iterable, mutable, can contain multiple data types

# In[51]:


# create an empty list (two ways)
empty_list = []
empty_list = list()


# In[52]:


# create a list
simpsons = ['homer', 'marge', 'bart']


# **Examine a list:**

# In[53]:


# print element 0
simpsons[0]


# In[54]:


len(simpsons)


# **Modify a list (does not return the list):**

# In[55]:


# append element to end
simpsons.append('lisa')
simpsons


# In[56]:


# append multiple elements to end
simpsons.extend(['itchy', 'scratchy'])
simpsons


# In[57]:


# insert element at index 0 (shifts everything right)
simpsons.insert(0, 'maggie')
simpsons


# In[58]:


# search for first instance and remove it
simpsons.remove('bart')
simpsons


# In[59]:


# remove element 0 and return it
simpsons.pop(0)


# In[60]:


# remove element 0 (does not return it)
del simpsons[0]
simpsons


# In[61]:


# replace element 0
simpsons[0] = 'krusty'
simpsons


# In[62]:


# concatenate lists (slower than 'extend' method)
neighbors = simpsons + ['ned', 'rod', 'todd']
neighbors


# **Find elements in a list:**

# In[63]:


# counts the number of instances
simpsons.count('lisa')


# In[64]:


# returns index of first instance
simpsons.index('itchy')


# **List slicing:**

# In[65]:


weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']


# In[66]:


# element 0
weekdays[0]


# In[67]:


# elements 0 (inclusive) to 3 (exclusive)
weekdays[0:3]


# In[68]:


# starting point is implied to be 0
weekdays[:3]


# In[69]:


# elements 3 (inclusive) through the end
weekdays[3:]


# In[70]:


# last element
weekdays[-1]


# In[71]:


# every 2nd element (step by 2)
weekdays[::2]


# In[72]:


# backwards (step by -1)
weekdays[::-1]


# In[73]:


# alternative method for returning the list backwards
list(reversed(weekdays))


# **Sort a list in place (modifies but does not return the list):**

# In[74]:


simpsons.sort()
simpsons


# In[75]:


# sort in reverse
simpsons.sort(reverse=True)
simpsons


# In[76]:


# sort by a key
simpsons.sort(key=len)
simpsons


# **Return a sorted list (does not modify the original list):**

# In[77]:


sorted(simpsons)


# In[78]:


sorted(simpsons, reverse=True)


# In[79]:


sorted(simpsons, key=len)


# **Insert into an already sorted list, and keep it sorted:**

# In[80]:


num = [10, 20, 40, 50]
from bisect import insort
insort(num, 30)
num


# **Object references and copies:**

# In[81]:


# create a second reference to the same list
same_num = num


# In[82]:


# modifies both 'num' and 'same_num'
same_num[0] = 0
print(num)
print(same_num)


# In[83]:


# copy a list (two ways)
new_num = num[:]
new_num = list(num)


# **Examine objects:**

# In[84]:


num is same_num    # checks whether they are the same object


# In[85]:


num is new_num


# In[86]:


num == same_num    # checks whether they have the same contents


# In[87]:


num == new_num


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 7. Tuples
# 
# - **Tuple properties:** ordered, iterable, immutable, can contain multiple data types
# - Like lists, but they don't change size

# In[88]:


# create a tuple directly
digits = (0, 1, 'two')


# In[89]:


# create a tuple from a list
digits = tuple([0, 1, 'two'])


# In[90]:


# trailing comma is required to indicate it's a tuple
zero = (0,)


# **Examine a tuple:**

# In[91]:


digits[2]


# In[92]:


len(digits)


# In[93]:


# counts the number of instances of that value
digits.count(0)


# In[94]:


# returns the index of the first instance of that value
digits.index(1)


# **Modify a tuple:**

# In[95]:


# elements of a tuple cannot be modified (this would throw an error)
# digits[2] = 2


# In[96]:


# concatenate tuples
digits = digits + (3, 4)
digits


# **Other tuple operations:**

# In[97]:


# create a single tuple with elements repeated (also works with lists)
(3, 4) * 2


# In[98]:


# sort a list of tuples
tens = [(20, 60), (10, 40), (20, 30)]
sorted(tens)    # sorts by first element in tuple, then second element


# In[99]:


# tuple unpacking
bart = ('male', 10, 'simpson')    # create a tuple
(sex, age, surname) = bart        # assign three values at once
print(sex)
print(age)
print(surname)


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 8. Strings
# 
# - **String properties:** iterable, immutable

# In[100]:


# convert another data type into a string
s = str(42)
s


# In[101]:


# create a string directly
s = 'I like you'


# **Examine a string:**

# In[102]:


s[0]


# In[103]:


len(s)


# **String slicing is like list slicing:**

# In[104]:


s[:6]


# In[105]:


s[7:]


# In[106]:


s[-1]


# **Basic string methods (does not modify the original string):**

# In[107]:


s.lower()


# In[108]:


s.upper()


# In[109]:


s.startswith('I')


# In[110]:


s.endswith('you')


# In[111]:


# checks whether every character in the string is a digit
s.isdigit()


# In[112]:


# returns index of first occurrence, but doesn't support regex
s.find('like')


# In[113]:


# returns -1 since not found
s.find('hate')


# In[114]:


# replaces all instances of 'like' with 'love'
s.replace('like', 'love')


# **Split a string:**

# In[115]:


# split a string into a list of substrings separated by a delimiter
s.split(' ')


# In[116]:


# equivalent (since space is the default delimiter)
s.split()


# In[117]:


s2 = 'a, an, the'
s2.split(',')


# **Join or concatenate strings:**

# In[118]:


# join a list of strings into one string using a delimiter
stooges = ['larry', 'curly', 'moe']
' '.join(stooges)


# In[119]:


# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4


# **Remove whitespace from the start and end of a string:**

# In[120]:


s5 = '  ham and cheese  '
s5.strip()


# **String substitutions:**

# In[121]:


# old way
'raining %s and %s' % ('cats', 'dogs')


# In[122]:


# new way
'raining {} and {}'.format('cats', 'dogs')


# In[123]:


# new way (using named arguments)
'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs')


# **String formatting ([more examples](https://mkaz.tech/python-string-format.html)):**

# In[124]:


# use 2 decimal places
'pi is {:.2f}'.format(3.14159)


# **Normal strings versus raw strings:**

# In[125]:


# normal strings allow for escaped characters
print('first line\nsecond line')


# In[126]:


# raw strings treat backslashes as literal characters
print(r'first line\nfirst line')


# **F strings**

# In[127]:


# basic f-string (Formatted string literals)
a = 10
print(f'a value is {a}')


# In[128]:


import math
print(f'The value of pi is approximately {math.pi:.3f}')


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 9. Dictionaries
# 
# - **Dictionary properties:** unordered, iterable, mutable, can contain multiple data types
# - Made of key-value pairs
# - Keys must be unique, and can be strings, numbers, or tuples
# - Values can be any type

# In[129]:


# create an empty dictionary (two ways)
empty_dict = {}
empty_dict = dict()


# In[130]:


# create a dictionary (two ways)
family = {'dad':'homer', 'mom':'marge', 'size':6}
family = dict(dad='homer', mom='marge', size=6)
family


# In[131]:


# convert a list of tuples into a dictionary
list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
family = dict(list_of_tuples)
family


# **Examine a dictionary:**

# In[132]:


# pass a key to return its value
family['dad']


# In[133]:


# return the number of key-value pairs
len(family)


# In[134]:


# check if key exists in dictionary
'mom' in family


# In[135]:


# dictionary values are not checked
'marge' in family


# In[136]:


# returns a list of keys (Python 2) or an iterable view (Python 3)
family.keys()


# In[137]:


# returns a list of values (Python 2) or an iterable view (Python 3)
family.values()


# In[138]:


# returns a list of key-value pairs (Python 2) or an iterable view (Python 3)
family.items()


# **Modify a dictionary (does not return the dictionary):**

# In[139]:


# add a new entry
family['cat'] = 'snowball'
family


# In[140]:


# edit an existing entry
family['cat'] = 'snowball ii'
family


# In[141]:


# delete an entry
del family['cat']
family


# In[142]:


# dictionary value can be a list
family['kids'] = ['bart', 'lisa']
family


# In[143]:


# remove an entry and return the value
family.pop('dad')


# In[144]:


# add multiple entries
family.update({'baby':'maggie', 'grandpa':'abe'})
family


# **Access values more safely with `get`:**

# In[145]:


family['mom']


# In[146]:


# equivalent to a dictionary lookup
family.get('mom')


# In[147]:


# this would throw an error since the key does not exist
# family['grandma']


# In[148]:


# return None if not found
family.get('grandma')


# In[149]:


# provide a default return value if not found
family.get('grandma', 'not found')


# **Access a list element within a dictionary:**

# In[150]:


family['kids'][0]


# In[151]:


family['kids'].remove('lisa')
family


# **String substitution using a dictionary:**

# In[152]:


'youngest child is %(baby)s' % family


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 10. Sets
# 
# - **Set properties:** unordered, iterable, mutable, can contain multiple data types
# - Made of unique elements (strings, numbers, or tuples)
# - Like dictionaries, but with keys only (no values)

# In[153]:


# create an empty set
empty_set = set()


# In[154]:


# create a set directly
languages = {'python', 'r', 'java'}


# In[155]:


# create a set from a list
snakes = set(['cobra', 'viper', 'python'])


# **Examine a set:**

# In[156]:


len(languages)


# In[157]:


'python' in languages


# **Set operations:**

# In[158]:


# intersection
languages & snakes


# In[159]:


# union
languages | snakes


# In[160]:


# set difference
languages - snakes


# In[161]:


# set difference
snakes - languages


# **Modify a set (does not return the set):**

# In[162]:


# add a new element
languages.add('sql')
languages


# In[163]:


# try to add an existing element (ignored, no error)
languages.add('r')
languages


# In[164]:


# remove an element
languages.remove('java')
languages


# In[165]:


# try to remove a non-existing element (this would throw an error)
# languages.remove('c')


# In[166]:


# remove an element if present, but ignored otherwise
languages.discard('c')
languages


# In[167]:


# remove and return an arbitrary element
languages.pop()


# In[168]:


# remove all elements
languages.clear()
languages


# In[169]:


# add multiple elements (can also pass a set)
languages.update(['go', 'spark'])
languages


# **Get a sorted list of unique elements from a list:**

# In[170]:


sorted(set([9, 0, 2, 1, 0]))


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 11. Defining Functions

# **Define a function with no arguments and no return values:**

# In[171]:


def print_text():
    print('this is text')


# In[172]:


# call the function
print_text()


# **Define a function with one argument and no return values:**

# In[173]:


def print_this(x):
    print(x)


# In[174]:


# call the function
print_this(3)


# In[175]:


# prints 3, but doesn't assign 3 to n because the function has no return statement
n = print_this(3)


# **Define a function with one argument and one return value:**

# In[176]:


def square_this(x):
    return x**2


# In[177]:


# include an optional docstring to describe the effect of a function
def square_this(x):
    """Return the square of a number."""
    return x**2


# In[178]:


# call the function
square_this(3)


# In[179]:


# assigns 9 to var, but does not print 9
var = square_this(3)


# **Define a function with two 'positional arguments' (no default values) and one 'keyword argument' (has a default value):**
# 

# In[180]:


def calc(a, b, op='add'):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    else:
        print('valid operations are add and sub')


# In[181]:


# call the function
calc(10, 4, op='add')


# In[182]:


# unnamed arguments are inferred by position
calc(10, 4, 'add')


# In[183]:


# default for 'op' is 'add'
calc(10, 4)


# In[184]:


calc(10, 4, 'sub')


# In[185]:


calc(10, 4, 'div')


# **Use `pass` as a placeholder if you haven't written the function body:**

# In[186]:


def stub():
    pass


# **Return two values from a single function:**

# In[187]:


def min_max(nums):
    return min(nums), max(nums)


# In[188]:


# return values can be assigned to a single variable as a tuple
nums = [1, 2, 3]
min_max_num = min_max(nums)
min_max_num


# In[189]:


# return values can be assigned into multiple variables using tuple unpacking
min_num, max_num = min_max(nums)
print(min_num)
print(max_num)


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 12. Anonymous (Lambda) Functions
# 
# - Primarily used to temporarily define a function for use by another function

# In[190]:


# define a function the "usual" way
def squared(x):
    return x**2


# In[191]:


# define an identical function using lambda
squared = lambda x: x**2


# **Sort a list of strings by the last letter:**

# In[192]:


# without using lambda
simpsons = ['homer', 'marge', 'bart']
def last_letter(word):
    return word[-1]
sorted(simpsons, key=last_letter)


# In[193]:


# using lambda
sorted(simpsons, key=lambda word: word[-1])


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 13. For Loops and While Loops

# **`range` returns a list of integers (Python 2) or a sequence (Python 3):**

# In[194]:


# includes the start value but excludes the stop value
range(0, 3)


# In[195]:


# default start value is 0
range(3)


# In[196]:


# third argument is the step value
range(0, 5, 2)


# In[197]:


# Python 2 only: use xrange to create a sequence rather than a list (saves memory)
# xrange(100, 100000, 5)


# **`for` loops:**

# In[198]:


# not the recommended style
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i].upper())


# In[199]:


# recommended style
for fruit in fruits:
    print(fruit.upper())


# In[200]:


# iterate through two things at once (using tuple unpacking)
family = {'dad':'homer', 'mom':'marge', 'size':6}
for key, value in family.items():
    print(key, value)


# In[201]:


# use enumerate if you need to access the index value within the loop
for index, fruit in enumerate(fruits):
    print(index, fruit)


# **`for`/`else` loop:**

# In[202]:


for fruit in fruits:
    if fruit == 'banana':
        print('Found the banana!')
        break    # exit the loop and skip the 'else' block
else:
    # this block executes ONLY if the for loop completes without hitting 'break'
    print("Can't find the banana")


# **`while` loop:**

# In[203]:


count = 0
while count < 5:
    print('This will print 5 times')
    count += 1    # equivalent to 'count = count + 1'


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 14. Comprehensions

# **List comprehension:**

# In[204]:


# for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num**3)
cubes


# In[205]:


# equivalent list comprehension
cubes = [num**3 for num in nums]
cubes


# In[206]:


# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)
cubes_of_even


# In[207]:


# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes_of_even = [num**3 for num in nums if num % 2 == 0]
cubes_of_even


# In[208]:


# for loop to cube even numbers and square odd numbers
cubes_and_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_and_squares.append(num**3)
    else:
        cubes_and_squares.append(num**2)
cubes_and_squares


# In[209]:


# equivalent list comprehension (using a ternary expression)
# syntax: [true_condition if condition else false_condition for variable in iterable]
cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]
cubes_and_squares


# In[210]:


# for loop to flatten a 2d-matrix
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)
items


# In[211]:


# equivalent list comprehension
items = [item for row in matrix
              for item in row]
items


# **Set comprehension:**

# In[212]:


fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}
unique_lengths


# **Dictionary comprehension:**

# In[213]:


fruit_lengths = {fruit:len(fruit) for fruit in fruits}
fruit_lengths


# In[214]:


fruit_indices = {fruit:index for index, fruit in enumerate(fruits)}
fruit_indices


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]

# ## 15. Map and Filter

# **`map` applies a function to every element of a sequence and returns a list (Python 2) or iterator (Python 3):**

# In[215]:


simpsons = ['homer', 'marge', 'bart']
map(len, simpsons)


# In[216]:


# equivalent list comprehension
[len(word) for word in simpsons]


# In[217]:


map(lambda word: word[-1], simpsons)


# In[218]:


# equivalent list comprehension
[word[-1] for word in simpsons]


# **`filter` returns a list (Python 2) or iterator (Python 3) containing the elements from a sequence for which a condition is `True`:**

# In[219]:


nums = range(5)
filter(lambda x: x % 2 == 0, nums)


# In[220]:


# equivalent list comprehension
[num for num in nums if num % 2 == 0]


# [<a href="#Python-Quick-Reference-by-Data-School">Back to top</a>]
