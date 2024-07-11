'''

Assignment 7.1
Write a program that prompts for a file name, then opens that file and reads through the file, 
and print the contents of the file in upper case. 
Use the file words.txt as the file name. You can download the sample data at:
http://www.py4e.com/code3/words.txt

'''

file = input("Enter the file name: ")
handle = open(file)
#   This doesn't actually works in my computer as I didn't provide the exact path
#   But works in the assignment


for line in handle:
    line = line.rstrip().upper()
    print(line)
