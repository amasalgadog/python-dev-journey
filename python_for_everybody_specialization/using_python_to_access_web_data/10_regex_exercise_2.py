#   this program will have different kind of regular expressions for practice
#   the function findall() will be used for searching and extracting substrings

import re

#   first group of strings
v = ' 22 street jump'
w = 'Is there a 23 version coming up? I hope for the ticket be less than $4.00'
x = 'From name.surname@domain.py 09:22:00 Sat Jul 2024'
y = 'From: second-name.last-name@domain.py: date'
z = 'From: 22/07/1991'

#   second group of strings
a = 'X-Sieve: ...'
b = 'X-DSPAM-Result: ...'
c = 'X-DSPAM-Confidence: ...'
d = 'X-Content-Type-Message-Body: ...'
e = 'X-Plane is behind schedule: ...'

#   create two lists for the previous strings
first_list = [v, w, x, y, z]
second_list = [a, b, c, d, e]

#   extract the digits from first group
temp_list = list()

for item in first_list:
    if re.search('[0-9]', item):
        stuff = re.findall('[0-9]+', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the email 1 - extract the exact regex
temp_list = list()

for item in first_list:
    if re.search('@', item):
        stuff = re.findall('\S+@\S+', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the email 2 - search a substring but extract only a portion of it
temp_list = list()

for item in first_list:
    if re.search('@', item):
        stuff = re.findall('^From (\S+@\S+)', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the email 3 - one or more times non-whitespaces
temp_list = list()

for item in first_list:
    if re.search('@', item):
        stuff = re.findall('^From: (\S+@\S+)', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the email 4 - non-greedy zero or more times non-whitespaces
temp_list = list()

for item in first_list:
    if re.search('@', item):
        stuff = re.findall('\S+?@\S*?', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the email 5 - non-greedy one or more times non-whitespaces
temp_list = list()

for item in first_list:
    if re.search('@', item):
        stuff = re.findall('\S+?@\S+?', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the domain of the email
temp_list = list()

for item in first_list:
    if re.search('@', item):
        stuff = re.findall('@([^ ]*)', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the price of ticket 1 - non-greedy one or more
temp_list = list()

for item in first_list:
    if re.search('\$', item):
        stuff = re.findall('\$[0-9.]+?', item)  
        #   if you remove '+?' you get the same result
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract the price of ticket 2 - one or more 
temp_list = list()

for item in first_list:
    if re.search('\$', item):
        stuff = re.findall('\$[0-9.]+', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract X strings
temp_list = list()

for item in second_list:
    if re.search('^X', item):
        stuff = re.findall('^X.*', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)

#   extract X-<something>: strings
temp_list = list()

for item in second_list:
    if re.search('^X', item):
        stuff = re.findall('^X-\S+:', item)
        if len(stuff) == 1:
            temp_list.append(stuff[0])
            continue
        for digit in stuff:
            temp_list.append(digit)

print(temp_list)