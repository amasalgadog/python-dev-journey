'''

Assignment 5.2 
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.

Invalid input
Maximum is 10
Minimum is 2

'''

largest = None
smallest = None

while True:
    s_value = input('Enter an integer: ')
    
    if s_value == 'done':
        print('Maximum is' ,largest)
        print('Minimum is' ,smallest)
        break
    else:
        try:
            i_value = int(s_value)
            
            if largest is None or smallest is None:
                largest = i_value
                smallest = i_value
            elif largest < i_value:
                largest = i_value
            elif smallest > i_value:
                smallest = i_value
        except:
            print('Invalid input')
            