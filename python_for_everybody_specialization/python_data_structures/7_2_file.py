'''

Assignment 7.2
Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute 
the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at:
http://www.py4e.com/code3/mbox-short.txt 

When you are testing below enter mbox-short.txt as the file name.

'''

file = input('Enter file name: ')
handle = open(file)
#   This doesn't actually works in my computer as I didn't provide the exact path
#   But works in the assignment
count = 0
total = 0
criteria = 'X-DSPAM-Confidence:'

for line in handle:
    if line.startswith(criteria):
        count += 1
        line = line[len(criteria):].strip()
        total += float(line)

average = total/count
print('Average spam confidence:', average)
