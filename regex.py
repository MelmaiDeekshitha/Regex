

import re
inp=input("enter string:")

pattern1 = '\d+'
'''re.findall()
The re.findall() method returns a list of strings containing all matches.'''
a = re.findall(pattern1, inp) 
print(a)
'''re.split()

The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.'''
b = re.split(pattern1, inp) 
print(b)

'''re.sub()

The method returns a string where matched occurrences are replaced with the content of replace variable.'''


# matches all whitespace characters
pattern2 = '\s+'

# empty string
replace = 'hi'

c = re.sub(pattern2, replace, inp) 
print(c)

# re.search()
match = re.search('\Ahello', inp)

if match:
  print("got match case")
else:
  print("no match case") 

'''match.group()

The group() method returns the part of the string where there is a match.
# four digit number followed by space followed by three  digit number'''
pattern3 = '(\d{4}) (\d{3})'

# match variable contains a Match object.
match = re.search(pattern3, inp) 

if match:
  print(match.group())
else:
  print("pattern not found")
