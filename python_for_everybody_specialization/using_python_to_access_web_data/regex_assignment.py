'''

Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_2049589.txt (There are 72 values and the sum ends with 205)

Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers and summing up the integers.

'''

import re

file_sample = 'python_for_everybody_specialization/using_python_to_access_web_data/regex_sum_42.txt'
file_actual = 'python_for_everybody_specialization/using_python_to_access_web_data/regex_sum_2049589.txt'
handle = open(file_actual)
haystack = list()
count = 0

#   regex need for check digits [0-9]+
for line in handle:
    line = line.rstrip()
    if re.search('[0-9]+', line):
        stuff = re.findall('[0-9]+', line)
        if len(stuff) == 1:
            haystack.append(int(stuff[0]))
            count += 1
        else:
            for number in stuff:
                haystack.append(int(number))
                count += 1

#   checking the values
#   print(haystack)
print(sum(haystack))
print(count)