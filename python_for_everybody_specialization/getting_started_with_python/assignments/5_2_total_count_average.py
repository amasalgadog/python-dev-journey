'''

Exercise 5-2
Write a program which repeatedly reads numbers until the user enter 'done'
Once 'done' is entered, print the total, count and average of the numbres.
If the user enters anything other than a number, detect their mistake with
try and except and print an error message and skip to the next number

'''
total = 0
average = 0
count = 0

while True:
    s_value = input('Enter a number: ')
    
    if s_value == 'done':
        print(total, count, average)
        break
    else:
        try:
            i_value = int(s_value)
            count += 1
            total += i_value
            average = total/count
        except:
            print('Error: data input not supported')
            # continue
    
    