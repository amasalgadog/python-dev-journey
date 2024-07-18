#   This program will return the maximum confidence value in the file.
#   These values can be found next to 'X-DSPAM-Confidence: ' in float format

#   import regular expressions module
import re

handle = open('python_for_everybody_specialization/using_python_to_access_web_data/mbox-short.txt')
numlist = list()

for line in handle:
    line = line.rstrip()

    #   Match the beginning with 'X-DSPAM-Confidence: '
    #   And extract just the digits and point characters one or more times from line
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum Confidence:', max(numlist))