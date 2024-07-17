'''

Assignment 9.4
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

'''

file = input("Enter file name: ")
#   This doesn't actually works in my computer as I didn't provide the exact path
#   But works in the assignment

handle = open(file)
database = dict()

for line in handle:
    if 'From ' not in line:
        continue
    words = line.split()
    person = words[1]        
    database[person] = database.get(person,0) + 1

max_name = None
max_count = None
for name, count in database.items():
    if max_name is None or count > max_count:
        max_name = name
        max_count = count

print(max_name, max_count)
        
