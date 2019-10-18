[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **DEDA_Introduction** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet : DEDA_Introduction
Published in : Digital Economy and Decision Analytics
Description : Introduce basic syntax, like numeric and string, and basic data structure, like list, tuple, set and dict in Python
Keywords : 
- Python
- Teaching
- Data Science
- Economy
- Decision
Author : Junjie Hu












```

### IPYNB Code
```ipynb

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Basic Syntax and Data Structure Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numeric operation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3\n",
      "10\n",
      "3.3333\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "try basic operations:\n",
    "+, -, *, /, %, **, //\n",
    "\"\"\"\n",
    "a = 5\n",
    "print(a)\n",
    "b = 3\n",
    "print(b)\n",
    "a *= 2\n",
    "print(a)\n",
    "c = round(a / b, 4)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "1020\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "d = '10'\n",
    "print(d)\n",
    "e = '20'\n",
    "print(e)\n",
    "f = d + e\n",
    "print(f)\n",
    "g = int(d) + int(e)\n",
    "print(g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Python provides a straight way for numerical operations\n",
    "Try comparison operationsL\n",
    "==,<,<=,>,>=,!=\n",
    "\"\"\"\n",
    "\n",
    "a = 5\n",
    "print(a == 5)  # True\n",
    "\n",
    "print(a <= 5)  # True\n",
    "print(a < 5)  # False\n",
    "\n",
    "a = 'A'\n",
    "b = 'B'\n",
    "print(a == b)  # False\n",
    "print(a != b)  # True\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Welcome', 'to', 'Python', 'World.', \"It's\", 'Amazing']\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "try comparision operations:\n",
    "==, <, <=, >, >=, !=\n",
    "\"\"\"\n",
    "\"\"\"\n",
    "string\n",
    "\"\"\"\n",
    "\"\"\"\n",
    "String is a basic type in python, it's common used and very powerful\n",
    "\"\"\"\n",
    "\n",
    "welcome_list = ['Welcome', 'to', 'Python', 'World.', 'It\\'s', 'Amazing']\n",
    "# using back slash to escape the single quote.\n",
    "\n",
    "print(welcome_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome\n",
      "to\n",
      "Python\n",
      "World.\n",
      "It's\n",
      "Amazing\n"
     ]
    }
   ],
   "source": [
    "# using for loop to iterate all elements in the list.\n",
    "for word in welcome_list:\n",
    "    print(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Python World. It's Amazing\n"
     ]
    }
   ],
   "source": [
    "# a string is also an object, using the join method to connect all the words in the list.\n",
    "welcome_sentence = ' '.join(welcome_list)\n",
    "print(welcome_sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to\n"
     ]
    }
   ],
   "source": [
    "# slicing string by indices.\n",
    "welcome_sliced = welcome_sentence[0:10]\n",
    "print(welcome_sliced)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Quiz: \n",
    "## Try changing the indices to negative."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WELCOME TO PYTHON WORLD. IT'S AMAZING\n"
     ]
    }
   ],
   "source": [
    "# see other methods of string object, like:\n",
    "welcome_upper_case = welcome_sentence.upper()\n",
    "print(welcome_upper_case)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on class str in module builtins:\n",
      "\n",
      "class str(object)\n",
      " |  str(object='') -> str\n",
      " |  str(bytes_or_buffer[, encoding[, errors]]) -> str\n",
      " |  \n",
      " |  Create a new string object from the given object. If encoding or\n",
      " |  errors is specified, then the object must expose a data buffer\n",
      " |  that will be decoded using the given encoding and error handler.\n",
      " |  Otherwise, returns the result of object.__str__() (if defined)\n",
      " |  or repr(object).\n",
      " |  encoding defaults to sys.getdefaultencoding().\n",
      " |  errors defaults to 'strict'.\n",
      " |  \n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __add__(self, value, /)\n",
      " |      Return self+value.\n",
      " |  \n",
      " |  __contains__(self, key, /)\n",
      " |      Return key in self.\n",
      " |  \n",
      " |  __eq__(self, value, /)\n",
      " |      Return self==value.\n",
      " |  \n",
      " |  __format__(...)\n",
      " |      S.__format__(format_spec) -> str\n",
      " |      \n",
      " |      Return a formatted version of S as described by format_spec.\n",
      " |  \n",
      " |  __ge__(self, value, /)\n",
      " |      Return self>=value.\n",
      " |  \n",
      " |  __getattribute__(self, name, /)\n",
      " |      Return getattr(self, name).\n",
      " |  \n",
      " |  __getitem__(self, key, /)\n",
      " |      Return self[key].\n",
      " |  \n",
      " |  __getnewargs__(...)\n",
      " |  \n",
      " |  __gt__(self, value, /)\n",
      " |      Return self>value.\n",
      " |  \n",
      " |  __hash__(self, /)\n",
      " |      Return hash(self).\n",
      " |  \n",
      " |  __iter__(self, /)\n",
      " |      Implement iter(self).\n",
      " |  \n",
      " |  __le__(self, value, /)\n",
      " |      Return self<=value.\n",
      " |  \n",
      " |  __len__(self, /)\n",
      " |      Return len(self).\n",
      " |  \n",
      " |  __lt__(self, value, /)\n",
      " |      Return self<value.\n",
      " |  \n",
      " |  __mod__(self, value, /)\n",
      " |      Return self%value.\n",
      " |  \n",
      " |  __mul__(self, value, /)\n",
      " |      Return self*value.n\n",
      " |  \n",
      " |  __ne__(self, value, /)\n",
      " |      Return self!=value.\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from builtins.type\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  __rmod__(self, value, /)\n",
      " |      Return value%self.\n",
      " |  \n",
      " |  __rmul__(self, value, /)\n",
      " |      Return self*value.\n",
      " |  \n",
      " |  __sizeof__(...)\n",
      " |      S.__sizeof__() -> size of S in memory, in bytes\n",
      " |  \n",
      " |  __str__(self, /)\n",
      " |      Return str(self).\n",
      " |  \n",
      " |  capitalize(...)\n",
      " |      S.capitalize() -> str\n",
      " |      \n",
      " |      Return a capitalized version of S, i.e. make the first character\n",
      " |      have upper case and the rest lower case.\n",
      " |  \n",
      " |  casefold(...)\n",
      " |      S.casefold() -> str\n",
      " |      \n",
      " |      Return a version of S suitable for caseless comparisons.\n",
      " |  \n",
      " |  center(...)\n",
      " |      S.center(width[, fillchar]) -> str\n",
      " |      \n",
      " |      Return S centered in a string of length width. Padding is\n",
      " |      done using the specified fill character (default is a space)\n",
      " |  \n",
      " |  count(...)\n",
      " |      S.count(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the number of non-overlapping occurrences of substring sub in\n",
      " |      string S[start:end].  Optional arguments start and end are\n",
      " |      interpreted as in slice notation.\n",
      " |  \n",
      " |  encode(...)\n",
      " |      S.encode(encoding='utf-8', errors='strict') -> bytes\n",
      " |      \n",
      " |      Encode S using the codec registered for encoding. Default encoding\n",
      " |      is 'utf-8'. errors may be given to set a different error\n",
      " |      handling scheme. Default is 'strict' meaning that encoding errors raise\n",
      " |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and\n",
      " |      'xmlcharrefreplace' as well as any other name registered with\n",
      " |      codecs.register_error that can handle UnicodeEncodeErrors.\n",
      " |  \n",
      " |  endswith(...)\n",
      " |      S.endswith(suffix[, start[, end]]) -> bool\n",
      " |      \n",
      " |      Return True if S ends with the specified suffix, False otherwise.\n",
      " |      With optional start, test S beginning at that position.\n",
      " |      With optional end, stop comparing S at that position.\n",
      " |      suffix can also be a tuple of strings to try.\n",
      " |  \n",
      " |  expandtabs(...)\n",
      " |      S.expandtabs(tabsize=8) -> str\n",
      " |      \n",
      " |      Return a copy of S where all tab characters are expanded using spaces.\n",
      " |      If tabsize is not given, a tab size of 8 characters is assumed.\n",
      " |  \n",
      " |  find(...)\n",
      " |      S.find(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the lowest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Return -1 on failure.\n",
      " |  \n",
      " |  format(...)\n",
      " |      S.format(*args, **kwargs) -> str\n",
      " |      \n",
      " |      Return a formatted version of S, using substitutions from args and kwargs.\n",
      " |      The substitutions are identified by braces ('{' and '}').\n",
      " |  \n",
      " |  format_map(...)\n",
      " |      S.format_map(mapping) -> str\n",
      " |      \n",
      " |      Return a formatted version of S, using substitutions from mapping.\n",
      " |      The substitutions are identified by braces ('{' and '}').\n",
      " |  \n",
      " |  index(...)\n",
      " |      S.index(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the lowest index in S where substring sub is found, \n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Raises ValueError when the substring is not found.\n",
      " |  \n",
      " |  isalnum(...)\n",
      " |      S.isalnum() -> bool\n",
      " |      \n",
      " |      Return True if all characters in S are alphanumeric\n",
      " |      and there is at least one character in S, False otherwise.\n",
      " |  \n",
      " |  isalpha(...)\n",
      " |      S.isalpha() -> bool\n",
      " |      \n",
      " |      Return True if all characters in S are alphabetic\n",
      " |      and there is at least one character in S, False otherwise.\n",
      " |  \n",
      " |  isdecimal(...)\n",
      " |      S.isdecimal() -> bool\n",
      " |      \n",
      " |      Return True if there are only decimal characters in S,\n",
      " |      False otherwise.\n",
      " |  \n",
      " |  isdigit(...)\n",
      " |      S.isdigit() -> bool\n",
      " |      \n",
      " |      Return True if all characters in S are digits\n",
      " |      and there is at least one character in S, False otherwise.\n",
      " |  \n",
      " |  isidentifier(...)\n",
      " |      S.isidentifier() -> bool\n",
      " |      \n",
      " |      Return True if S is a valid identifier according\n",
      " |      to the language definition.\n",
      " |      \n",
      " |      Use keyword.iskeyword() to test for reserved identifiers\n",
      " |      such as \"def\" and \"class\".\n",
      " |  \n",
      " |  islower(...)\n",
      " |      S.islower() -> bool\n",
      " |      \n",
      " |      Return True if all cased characters in S are lowercase and there is\n",
      " |      at least one cased character in S, False otherwise.\n",
      " |  \n",
      " |  isnumeric(...)\n",
      " |      S.isnumeric() -> bool\n",
      " |      \n",
      " |      Return True if there are only numeric characters in S,\n",
      " |      False otherwise.\n",
      " |  \n",
      " |  isprintable(...)\n",
      " |      S.isprintable() -> bool\n",
      " |      \n",
      " |      Return True if all characters in S are considered\n",
      " |      printable in repr() or S is empty, False otherwise.\n",
      " |  \n",
      " |  isspace(...)\n",
      " |      S.isspace() -> bool\n",
      " |      \n",
      " |      Return True if all characters in S are whitespace\n",
      " |      and there is at least one character in S, False otherwise.\n",
      " |  \n",
      " |  istitle(...)\n",
      " |      S.istitle() -> bool\n",
      " |      \n",
      " |      Return True if S is a titlecased string and there is at least one\n",
      " |      character in S, i.e. upper- and titlecase characters may only\n",
      " |      follow uncased characters and lowercase characters only cased ones.\n",
      " |      Return False otherwise.\n",
      " |  \n",
      " |  isupper(...)\n",
      " |      S.isupper() -> bool\n",
      " |      \n",
      " |      Return True if all cased characters in S are uppercase and there is\n",
      " |      at least one cased character in S, False otherwise.\n",
      " |  \n",
      " |  join(...)\n",
      " |      S.join(iterable) -> str\n",
      " |      \n",
      " |      Return a string which is the concatenation of the strings in the\n",
      " |      iterable.  The separator between elements is S.\n",
      " |  \n",
      " |  ljust(...)\n",
      " |      S.ljust(width[, fillchar]) -> str\n",
      " |      \n",
      " |      Return S left-justified in a Unicode string of length width. Padding is\n",
      " |      done using the specified fill character (default is a space).\n",
      " |  \n",
      " |  lower(...)\n",
      " |      S.lower() -> str\n",
      " |      \n",
      " |      Return a copy of the string S converted to lowercase.\n",
      " |  \n",
      " |  lstrip(...)\n",
      " |      S.lstrip([chars]) -> str\n",
      " |      \n",
      " |      Return a copy of the string S with leading whitespace removed.\n",
      " |      If chars is given and not None, remove characters in chars instead.\n",
      " |  \n",
      " |  partition(...)\n",
      " |      S.partition(sep) -> (head, sep, tail)\n",
      " |      \n",
      " |      Search for the separator sep in S, and return the part before it,\n",
      " |      the separator itself, and the part after it.  If the separator is not\n",
      " |      found, return S and two empty strings.\n",
      " |  \n",
      " |  replace(...)\n",
      " |      S.replace(old, new[, count]) -> str\n",
      " |      \n",
      " |      Return a copy of S with all occurrences of substring\n",
      " |      old replaced by new.  If the optional argument count is\n",
      " |      given, only the first count occurrences are replaced.\n",
      " |  \n",
      " |  rfind(...)\n",
      " |      S.rfind(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the highest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Return -1 on failure.\n",
      " |  \n",
      " |  rindex(...)\n",
      " |      S.rindex(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the highest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Raises ValueError when the substring is not found.\n",
      " |  \n",
      " |  rjust(...)\n",
      " |      S.rjust(width[, fillchar]) -> str\n",
      " |      \n",
      " |      Return S right-justified in a string of length width. Padding is\n",
      " |      done using the specified fill character (default is a space).\n",
      " |  \n",
      " |  rpartition(...)\n",
      " |      S.rpartition(sep) -> (head, sep, tail)\n",
      " |      \n",
      " |      Search for the separator sep in S, starting at the end of S, and return\n",
      " |      the part before it, the separator itself, and the part after it.  If the\n",
      " |      separator is not found, return two empty strings and S.\n",
      " |  \n",
      " |  rsplit(...)\n",
      " |      S.rsplit(sep=None, maxsplit=-1) -> list of strings\n",
      " |      \n",
      " |      Return a list of the words in S, using sep as the\n",
      " |      delimiter string, starting at the end of the string and\n",
      " |      working to the front.  If maxsplit is given, at most maxsplit\n",
      " |      splits are done. If sep is not specified, any whitespace string\n",
      " |      is a separator.\n",
      " |  \n",
      " |  rstrip(...)\n",
      " |      S.rstrip([chars]) -> str\n",
      " |      \n",
      " |      Return a copy of the string S with trailing whitespace removed.\n",
      " |      If chars is given and not None, remove characters in chars instead.\n",
      " |  \n",
      " |  split(...)\n",
      " |      S.split(sep=None, maxsplit=-1) -> list of strings\n",
      " |      \n",
      " |      Return a list of the words in S, using sep as the\n",
      " |      delimiter string.  If maxsplit is given, at most maxsplit\n",
      " |      splits are done. If sep is not specified or is None, any\n",
      " |      whitespace string is a separator and empty strings are\n",
      " |      removed from the result.\n",
      " |  \n",
      " |  splitlines(...)\n",
      " |      S.splitlines([keepends]) -> list of strings\n",
      " |      \n",
      " |      Return a list of the lines in S, breaking at line boundaries.\n",
      " |      Line breaks are not included in the resulting list unless keepends\n",
      " |      is given and true.\n",
      " |  \n",
      " |  startswith(...)\n",
      " |      S.startswith(prefix[, start[, end]]) -> bool\n",
      " |      \n",
      " |      Return True if S starts with the specified prefix, False otherwise.\n",
      " |      With optional start, test S beginning at that position.\n",
      " |      With optional end, stop comparing S at that position.\n",
      " |      prefix can also be a tuple of strings to try.\n",
      " |  \n",
      " |  strip(...)\n",
      " |      S.strip([chars]) -> str\n",
      " |      \n",
      " |      Return a copy of the string S with leading and trailing\n",
      " |      whitespace removed.\n",
      " |      If chars is given and not None, remove characters in chars instead.\n",
      " |  \n",
      " |  swapcase(...)\n",
      " |      S.swapcase() -> str\n",
      " |      \n",
      " |      Return a copy of S with uppercase characters converted to lowercase\n",
      " |      and vice versa.\n",
      " |  \n",
      " |  title(...)\n",
      " |      S.title() -> str\n",
      " |      \n",
      " |      Return a titlecased version of S, i.e. words start with title case\n",
      " |      characters, all remaining cased characters have lower case.\n",
      " |  \n",
      " |  translate(...)\n",
      " |      S.translate(table) -> str\n",
      " |      \n",
      " |      Return a copy of the string S in which each character has been mapped\n",
      " |      through the given translation table. The table must implement\n",
      " |      lookup/indexing via __getitem__, for instance a dictionary or list,\n",
      " |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If\n",
      " |      this operation raises LookupError, the character is left untouched.\n",
      " |      Characters mapped to None are deleted.\n",
      " |  \n",
      " |  upper(...)\n",
      " |      S.upper() -> str\n",
      " |      \n",
      " |      Return a copy of S converted to uppercase.\n",
      " |  \n",
      " |  zfill(...)\n",
      " |      S.zfill(width) -> str\n",
      " |      \n",
      " |      Pad a numeric string S with zeros on the left, to fill a field\n",
      " |      of the specified width. The string S is never truncated.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  maketrans(x, y=None, z=None, /)\n",
      " |      Return a translation table usable for str.translate().\n",
      " |      \n",
      " |      If there is only one argument, it must be a dictionary mapping Unicode\n",
      " |      ordinals (integers) or characters to Unicode ordinals, strings or None.\n",
      " |      Character keys will be then converted to ordinals.\n",
      " |      If there are two arguments, they must be strings of equal length, and\n",
      " |      in the resulting dictionary, each character in x will be mapped to the\n",
      " |      character at the same position in y. If there is a third argument, it\n",
      " |      must be a string, whose characters will be mapped to None in the result.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# by using dir() function, or help() function\n",
    "dir(str)\n",
    "# likewise,\n",
    "help(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__add__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__getnewargs__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__mod__',\n",
       " '__mul__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__rmod__',\n",
       " '__rmul__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'capitalize',\n",
       " 'casefold',\n",
       " 'center',\n",
       " 'count',\n",
       " 'encode',\n",
       " 'endswith',\n",
       " 'expandtabs',\n",
       " 'find',\n",
       " 'format',\n",
       " 'format_map',\n",
       " 'index',\n",
       " 'isalnum',\n",
       " 'isalpha',\n",
       " 'isdecimal',\n",
       " 'isdigit',\n",
       " 'isidentifier',\n",
       " 'islower',\n",
       " 'isnumeric',\n",
       " 'isprintable',\n",
       " 'isspace',\n",
       " 'istitle',\n",
       " 'isupper',\n",
       " 'join',\n",
       " 'ljust',\n",
       " 'lower',\n",
       " 'lstrip',\n",
       " 'maketrans',\n",
       " 'partition',\n",
       " 'replace',\n",
       " 'rfind',\n",
       " 'rindex',\n",
       " 'rjust',\n",
       " 'rpartition',\n",
       " 'rsplit',\n",
       " 'rstrip',\n",
       " 'split',\n",
       " 'splitlines',\n",
       " 'startswith',\n",
       " 'strip',\n",
       " 'swapcase',\n",
       " 'title',\n",
       " 'translate',\n",
       " 'upper',\n",
       " 'zfill']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# or a str instance\n",
    "dir(welcome_upper_case)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hallo, JON. Welcome to Python World. It's Amazing\n"
     ]
    }
   ],
   "source": [
    "# formatting string\n",
    "greeting = 'Hallo'\n",
    "name = 'Jon'\n",
    "# using format method\n",
    "welcome_jon = '{}, {}. '.format(greeting, name.upper()) + welcome_sentence\n",
    "print(welcome_jon)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hallo, JON. Welcome to Python World. It's Amazing\n"
     ]
    }
   ],
   "source": [
    "# using f string, you can write variable name into brackets, directly.\n",
    "welcome_jon_f = f'{greeting}, {name.upper()}. ' + welcome_sentence\n",
    "print(welcome_jon_f)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Basic Data Structures"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Allan Lee', '06-04-2000', 'Male', 'U.S.A']\n",
      "('Jon Dow', '06-04-2000', 'Male', 'U.S.A')\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "tuple and set are two basic structures with different features to list.\n",
    "\"\"\"\n",
    "\n",
    "# tuple is like list, but tuple is immutable\n",
    "person_list = ['Jon Dow', '06-04-2000', 'Male', 'U.S.A']\n",
    "person_tuple = ('Jon Dow', '06-04-2000', 'Male', 'U.S.A')\n",
    "person_list[0] = 'Allan Lee'\n",
    "print(person_list)\n",
    "print(person_tuple)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### inmutable of tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-23-75dbd458f37d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# ! Error will happen, tuple is not mutable\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mperson_tuple\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'Allan Lee'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "# ! Error will happen, tuple is immutable\n",
    "person_tuple[0] = 'Allan Lee'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Totally 6 countries: {'Singapore', 'Korea', 'Japan', 'China', 'Russia', 'Turkey'}\n",
      "{'Singapore', 'Korea', 'Japan', 'China', 'Russia', 'Turkey'}\n"
     ]
    }
   ],
   "source": [
    "# \"Janpan\" shown twice\n",
    "countries_1 = {'China', 'Japan', 'Japan', 'Korea', 'Russia', 'Singapore', 'Turkey'}\n",
    "countries_2 = {'France', 'Germany', 'Italy', 'Russia', 'Spain', 'Turkey', 'UK', 'USA'}\n",
    "\n",
    "print(f'Totally {len(countries_1)} countries: {countries_1}')  # sets will drop duplicated elements automatically"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Russia', 'Turkey'}\n"
     ]
    }
   ],
   "source": [
    "count_inter = countries_1.intersection(countries_2)\n",
    "print(count_inter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Singapore', 'Korea', 'Japan', 'China'}\n"
     ]
    }
   ],
   "source": [
    "count_1_diff = countries_1.difference(countries_2)\n",
    "print(count_1_diff)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Spain', 'UK', 'Germany', 'France', 'Italy', 'USA'}\n"
     ]
    }
   ],
   "source": [
    "count_2_diff = countries_2.difference(countries_1)\n",
    "print(count_2_diff)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Spain', 'Singapore', 'Korea', 'Germany', 'UK', 'Japan', 'China', 'Russia', 'Turkey', 'France', 'Italy', 'USA'}\n"
     ]
    }
   ],
   "source": [
    "countries_new = countries_1.union(countries_2)\n",
    "print(countries_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# list\n",
    "\n",
    "### Using list makes Python code simple.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "how many elements in a list?\n",
      "3\n",
      "how many elements in a string?\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "natr_language = ['English', 'German', 'Chinese']\n",
    "prog_language = ['C++', 'Java', 'C#']\n",
    "\n",
    "print('how many elements in a list?')\n",
    "print(len(natr_language)) \n",
    "print('how many elements in a string?')\n",
    "print(len(natr_language[0]))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Basic operations of list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['English', 'German', 'Chinese', 'Spanish']\n",
      "['Python', 'C++', 'Java', 'C#']\n",
      "['Python', 'C++', 'Java', 'C#', ['python 2.7', 'python 3.6', 'python 3.7', 'python 3.8']]\n",
      "['English', 'German', 'Chinese', 'Spanish', 'Japanese', 'Korean']\n",
      "['Python', 'C++', 'Java', 'C#']\n",
      "['English', 'German', 'Chinese', 'Spanish', 'Japanese']\n",
      "['Python', 'C++', 'Java']\n"
     ]
    }
   ],
   "source": [
    "# adding elements into the list\n",
    "# append() allows you to add 1 element at the end of the list\n",
    "natr_language.append('Spanish')  # ['English', 'German', 'Chinese', 'Spanish']\n",
    "print(natr_language)\n",
    "# insert() allows you to add 1 element at arbitrary place\n",
    "prog_language.insert(0, 'Python')  # ['Python', 'C++', 'Java', 'C#']\n",
    "print(prog_language)\n",
    "\n",
    "# extend() allows you to add multiple elements at the end of the list\n",
    "python = ['python 2.7', 'python 3.6', 'python 3.7', 'python 3.8']\n",
    "prog_language.append(python)  # ['Python', 'C++', 'Java', 'C#', ['python 2.7', 'python 3.6']]\n",
    "print(prog_language)\n",
    "more_language = ['Japanese', 'Korean']\n",
    "natr_language.extend(more_language)  # ['English', 'German', 'Chinese', 'Spanish', 'Japanese', 'Korean']\n",
    "print(natr_language)\n",
    "\n",
    "# remove elements\n",
    "prog_language.remove(python)  # ['Python', 'C++', 'Java', 'C#']\n",
    "print(prog_language)\n",
    "natr_language.pop(-1)  # 'Korean' pops out. ['English', 'German', 'Chinese', 'Spanish', 'Japanese']\n",
    "print(natr_language)\n",
    "del prog_language[-1]  # ['Python', 'C++', 'Java']\n",
    "print(prog_language)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reverse Numbers: [22, 95, 32, 11, 43]\n",
      "Sort Numbers: [11, 22, 32, 43, 95]\n",
      "Reversed Sorting [95, 43, 32, 22, 11]\n",
      "Python\n",
      "C++\n",
      "Java\n",
      "0. English\n",
      "1. German\n",
      "2. Chinese\n",
      "3. Spanish\n",
      "4. Japanese\n",
      "English, German, Chinese, Spanish, Japanese\n",
      "['English', 'German', 'Chinese', 'Spanish', 'Japanese']\n"
     ]
    }
   ],
   "source": [
    "# reorder in list\n",
    "numbers = [43, 11, 32, 95, 22]\n",
    "numbers.reverse()\n",
    "print(f'Reverse Numbers: {numbers}')  # [22, 95, 32, 11, 43]\n",
    "numbers.sort()\n",
    "print(f'Sort Numbers: {numbers}')  # [11, 22, 32, 43, 95]\n",
    "numbers.sort(reverse=True)\n",
    "print(f'Reversed Sorting {numbers}')  # [95, 43, 32, 22, 11]\n",
    "\n",
    "sorted_number = sorted(numbers)  # sorted function can return a new list instead of altering the original list\n",
    "\n",
    "# basic search in list\n",
    "min_num = min(numbers)  # 11\n",
    "max_num = max(numbers)  # 95\n",
    "sum_num = sum(numbers)  # 203\n",
    "index_num = numbers.index(32)  # 2\n",
    "\n",
    "# iterate in list\n",
    "for lang in prog_language:\n",
    "    print(lang)\n",
    "# iterate in list with index\n",
    "for num, lang in enumerate(natr_language):\n",
    "    print(f'{num}. {lang}')\n",
    "\n",
    "# list to string\n",
    "natr_language_str = ', '.join(natr_language)  # 'Spanish, Japanese, German, English, Chinese'\n",
    "print(natr_language_str)\n",
    "natr_language_new = natr_language_str.split(', ')  # ['Spanish', 'Japanese', 'German', 'English', 'Chinese']\n",
    "print(natr_language_new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Iteration with list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Chinese', 'Japanese']\n",
      "Original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
      "Reformat: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']\n"
     ]
    }
   ],
   "source": [
    "# looping in the list. The basic syntax is:\n",
    "# [func(ele) for func(ele) in a_list if func(ele)]\n",
    "# For example:\n",
    "nations = [language for language in natr_language_new if language.endswith('ese')]\n",
    "print(nations)\n",
    "\n",
    "# format number in list to 2 digit\n",
    "num_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "num_seq_dd = [format(num, '02d') for num in num_seq]\n",
    "print(f'Original: {num_seq}')\n",
    "print(f'Reformat: {num_seq_dd}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 5, 7, 11]\n",
      "2\n",
      "11\n",
      "[2, 3]\n",
      "[5, 7, 11]\n",
      "['h', 'a', 'l', 'l', 'o']\n",
      "['a', 'h', 'l', 'l', 'o']\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Lists are versatile Python data structure to group values.\n",
    "Lists can contain different types, e.g. strings, numbers, \n",
    "functions, lists, ...\n",
    "\"\"\"\n",
    "p = [2, 3, 5, 7, 11]\n",
    "print(p)  # [2, 3, 5, 7, 11]\n",
    "\n",
    "# indexing\n",
    "print(p[0])  # 2\n",
    "print(p[-1])  # 11\n",
    "\n",
    "# slicing\n",
    "print(p[:2])  # [2, 3]\n",
    "print(p[-3:])  # [5, 7, 11]\n",
    "\n",
    "# appending\n",
    "p.append(13)  # [2, 3, 5, 7, 11, 13]\n",
    "p.extend([17, 19])  # [2, 3, 5, 7, 11, 13, 17, 19]\n",
    "\n",
    "l = list('hallo')  # ['h', 'a', 'l', 'l', 'o']\n",
    "print(l)\n",
    "l.sort()  # ['a', 'h', 'l', 'l', 'o']\n",
    "print(l)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Basic operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12345\n",
      "{'China': 8612, 'France': 39827, 'Germany': 44680, 'Italy': 32038, 'Japan': 38214, 'Korea': 29958, 'Russia': 10846, 'Turkey': 10498, 'UK': 39532, 'USA': 59939}\n",
      "dict_keys(['China', 'France', 'Germany', 'Italy', 'Japan', 'Korea', 'Russia', 'Turkey', 'UK', 'USA'])\n",
      "dict_values([8612, 39827, 44680, 32038, 38214, 29958, 10846, 10498, 39532, 59939])\n",
      "{'China': 8612, 'France': 39827, 'Germany': 44680, 'Italy': 32038, 'Japan': 38214, 'Korea': 29958, 'Russia': 10846, 'Turkey': 10498, 'UK': 39532, 'USA': 59939, 'Singapore': 56746, 'Spain': 28175}\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Dictionary: Essentially mapping keys to values\n",
    "\"\"\"\n",
    "\n",
    "# Creating a dictionary\n",
    "# GDP per capital (Nominal) 2017\n",
    "gdp_percap = {'China': 8612,\n",
    "              'France': 39827,\n",
    "              'Germany': 12345,  # dummy number\n",
    "              'Italy': 32038,\n",
    "              'Japan': 38214,\n",
    "              'Korea': 29958,\n",
    "              'Russia': 10846,\n",
    "              'Turkey': 10498,\n",
    "              'UK': 39532,\n",
    "              'USA': 59939}\n",
    "\n",
    "# Accessing\n",
    "print(f'{gdp_percap[\"Germany\"]}')  # 12345\n",
    "# Changing value\n",
    "gdp_percap['Germany'] = 44680\n",
    "print(gdp_percap)\n",
    "\n",
    "# Getting keys and values\n",
    "print(gdp_percap.keys())\n",
    "print(gdp_percap.values())\n",
    "\n",
    "# Adding more than 1 elements\n",
    "gdp_percap.update({'Singapore': 56746, 'Spain': 28175})\n",
    "print(gdp_percap)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Operations in Dictionary values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "min price: (8612, 'China')\n",
      "max price: (59939, 'USA')\n",
      "China: 8612\n",
      "Turkey: 10498\n",
      "Russia: 10846\n",
      "Spain: 28175\n",
      "Korea: 29958\n",
      "Italy: 32038\n",
      "Japan: 38214\n",
      "UK: 39532\n",
      "France: 39827\n",
      "Germany: 44680\n",
      "Singapore: 56746\n",
      "USA: 59939\n"
     ]
    }
   ],
   "source": [
    "# Given a dataset in dict form, operation by the values\n",
    "# Find min and max values by transforming to zip type\n",
    "min_value = min(zip(gdp_percap.values(), gdp_percap.keys()))\n",
    "max_value = max(zip(gdp_percap.values(), gdp_percap.keys()))\n",
    "\n",
    "print(f'min price: {min_value}')\n",
    "print(f'max price: {max_value}')\n",
    "\n",
    "# Sort elements by the values\n",
    "gdppc_sorted = sorted(zip(gdp_percap.values(), gdp_percap.keys()))\n",
    "for gdppc, country in gdppc_sorted:\n",
    "    print(f'{country}: {gdppc}')\n",
    "\n",
    "# Subset of a dictionary (Slicing dictionary by condition)\n",
    "gdp_subset = {key: value for key, value in gdp_percap.items() if value >= 30000}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## For loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 4 6 8 10 0 2 4 8 10 D E D A a has value 1\n",
      "b has value 2\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "For Loop can iterate over all iterables.\n",
    "All iterables have a method __iter__ which returns an iterator\n",
    "\"\"\"\n",
    "l = list([1, 2, 3, 4, 5])\n",
    "for i in l:\n",
    "    print(i * 2, end=' ')\n",
    "# 2 4 6 8 10\n",
    "\n",
    "for i in range(6):\n",
    "    if i == 3:\n",
    "        continue\n",
    "    print(i * 2, end=' ')\n",
    "# 0 2 4 8 10\n",
    "\n",
    "for i in 'DEDA':\n",
    "    print(i, end=' ')\n",
    "# D E D A\n",
    "\n",
    "d = dict(a=1, b=2)\n",
    "for k, v in d.items():\n",
    "    print('{} has value {}'.format(k, v))\n",
    "# a has value 1\n",
    "# b has value 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## While loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1 2 3 5 8 13 21 34 55 89 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "While loop\n",
    "There is no Do-While-Loop\n",
    "\"\"\"\n",
    "# Fibonacci series: sum of two preceding numbers defines next number\n",
    "\n",
    "a, b = 0, 1\n",
    "while b < 100:\n",
    "    print(b, end=' ')\n",
    "    a, b = b, b + a\n",
    "# 1 1 2 3 5 8 13 21 34 55 89\n",
    "# ATTENTION: Make sure not to have infinite loop (loop with tautology in condition)\n",
    "\n",
    "# Do While Loop\n",
    "fib = [0, 1]\n",
    "while True:\n",
    "    fib.append(sum(fib[-2:]))\n",
    "    if fib[-1] > 100:\n",
    "        break\n",
    "print(fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Condition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive value\n",
      "True\n",
      "False\n",
      "True\n",
      "Value x is not None\n",
      "Value x is not None\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Control Flow Tools: if/elif/else\n",
    "\"\"\"\n",
    "x = 10\n",
    "if x < 0:\n",
    "    print('Negative value')\n",
    "elif x == 0:\n",
    "    print('Zero')\n",
    "else:\n",
    "    print('Positive value')\n",
    "# Positive value\n",
    "\n",
    "# Conditions can be combined or altered with: and, or, not, is, is not\n",
    "# Comparision statements can be used\n",
    "p = [2, 3, 5, 7, 11]\n",
    "print(3 in p)  # True\n",
    "print(3 in p and 4 in p)  # False\n",
    "print(3 in p or 4 in p)  # True\n",
    "if x is not None:\n",
    "    print('Value x is not None')\n",
    "# Alternative\n",
    "if not x is None:\n",
    "    print('Value x is not None')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Definef function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 9, 16, 25]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Function definition\n",
    "\"\"\"\n",
    "\n",
    "\n",
    "def square_numeric(x):\n",
    "    \"\"\" Squares numeric x\"\"\"\n",
    "    return x ** 2\n",
    "\n",
    "\n",
    "def square_iterable(x):\n",
    "    \"\"\" Squares numerics in iterable x\"\"\"\n",
    "    ret = []\n",
    "    for i in x:\n",
    "        ret.append(square_numeric(i))\n",
    "    return ret\n",
    "\n",
    "\n",
    "def square_iterabel_short(x):\n",
    "    \"\"\" Squares numerics in iterable x\"\"\"\n",
    "    return [square_numeric(i) for i in x]\n",
    "\n",
    "\n",
    "x = [1, 2, 3, 4, 5]\n",
    "square_iterable(x)  # [1, 4, 9, 16, 25]\n",
    "square_iterabel_short(x)  # [1, 4, 9, 16, 25]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Application: Wiggling Elephant Trunk"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wiggling Elephant Trunk\n",
    "\n",
    "vonNeuman_elephant.py\n",
    "    \"With four parameters I can fit an elephant,\n",
    "       and with five I can make him wiggle his trunk.\"\n",
    "\n",
    "Original Versions:\n",
    "\n",
    "    Author[1]: Piotr A. Zolnierczuk (zolnierczukp at ornl dot gov)\n",
    "    Retrieved on 14 September 2011 from\n",
    "    http://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant/\n",
    "Modified to wiggle trunk:\n",
    "    2 October 2011 by David Bailey (http://www.physics.utoronto.ca/~dbailey)\n",
    "\n",
    "    Author[2]:\n",
    "    Advanced Physics Laboratory\n",
    "    https://www.physics.utoronto.ca/~phy326/python/\n",
    "\n",
    "Based on the paper:\n",
    "    \"Drawing an elephant with four complex parameters\", by\n",
    "    Jurgen Mayer, Khaled Khairy, and Jonathon Howard,\n",
    "    Am. J. Phys. 78, 648 (2010), DOI:10.1119/1.3254017\n",
    "\n",
    "    The paper does not specify how the wiggle parameter controls the\n",
    "    trunk, so a guess was made.\n",
    "\n",
    "Inspired by John von Neumann's famous quote (above) about overfitting data.\n",
    "    Attributed to von Neumann by Enrico Fermi, as quoted by\n",
    "      Freeman Dyson in \"A meeting with Enrico Fermi\" in\n",
    "      Nature 427 (22 January 2004) p. 297\n",
    "      \n",
    "Python Version: 3.6\n",
    "Modified based on author[2]'s work\n",
    "Author: Junjie Hu\n",
    "\n",
    "Overfiting problem in trading strategy stated:\n",
    "Bailey, D., Borwein, J., Lopez de Prado, M., & Zhu, Q. (2014).\n",
    "Pseudo-mathematics and financial charlatanism: The effects of backtest overfitting on out-of-sample performance.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# %matplotlib tk\n",
    "%matplotlib inline\n",
    "# %matplotlib nbagg\n",
    "import matplotlib\n",
    "# plt.rcParams[\"animation.html\"] = \"html5\"\n",
    "\n",
    "from matplotlib import animation\n",
    "from numpy import append, cos, linspace, pi, sin, zeros\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# elephant parameters\n",
    "parameters = [50 - 30j, 18 + 8j, 12 - 10j, -14 - 60j, 20 + 20j]\n",
    "\n",
    "\n",
    "def fourier(t, C):\n",
    "    f = zeros(t.shape)\n",
    "    for k in range(len(C)):\n",
    "        f += C.real[k] * cos(k * t) + C.imag[k] * sin(k * t)\n",
    "    return f\n",
    "\n",
    "\n",
    "def elephant(t, p):\n",
    "    npar = 6\n",
    "\n",
    "    Cx = zeros((npar,), dtype='complex')\n",
    "    Cy = zeros((npar,), dtype='complex')\n",
    "\n",
    "    Cx[1] = p[0].real * 1j\n",
    "    Cy[1] = p[3].imag + p[0].imag * 1j\n",
    "\n",
    "    Cx[2] = p[1].real * 1j\n",
    "    Cy[2] = p[1].imag * 1j\n",
    "\n",
    "    Cx[3] = p[2].real\n",
    "    Cy[3] = p[2].imag * 1j\n",
    "\n",
    "    Cx[5] = p[3].real\n",
    "\n",
    "    x = append(fourier(t, Cy), [p[4].imag])\n",
    "    y = -append(fourier(t, Cx), [-p[4].imag])\n",
    "\n",
    "    return x, y\n",
    "\n",
    "\n",
    "def init_plot():\n",
    "    # draw the body of the elephant\n",
    "    # create trunk\n",
    "    x, y = elephant(linspace(2 * pi + 0.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)\n",
    "    for ii in range(len(y) - 1):\n",
    "        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(0)) * parameters[4].real\n",
    "    trunk.set_data(x, y)\n",
    "    return trunk,\n",
    "\n",
    "\n",
    "def move_trunk(i):\n",
    "    x, y = elephant(linspace(2 * pi + 0.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)\n",
    "    # move trunk to new position (but don't move eye stored at end or array)\n",
    "    for ii in range(len(y) - 1):\n",
    "        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(i)) * parameters[4].real\n",
    "    trunk.set_data(x, y)\n",
    "    return trunk,\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots()\n",
    "# initial the elephant body\n",
    "x, y = elephant(t=linspace(0.4 + 1.3 * pi, 2 * pi + 0.9 * pi, 1000), p=parameters)\n",
    "plt.plot(x, y, 'b.')\n",
    "plt.xlim([-75, 90])\n",
    "plt.ylim([-70, 87])\n",
    "plt.axis('off')\n",
    "trunk, = ax.plot([], [], 'b.')  # initialize trunk\n",
    "\n",
    "ani = animation.FuncAnimation(fig=fig,\n",
    "                              func=move_trunk,\n",
    "                              frames=1000,\n",
    "                              init_func=init_plot,\n",
    "                              interval=500,\n",
    "                              blit=False,\n",
    "                              repeat=True)\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

```

automatically created on 2019-10-18

### PYTHON Code
```python

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

import matplotlib

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
                              interval=500,
                              blit=False,
                              repeat=True)
plt.show()

```

automatically created on 2019-10-18