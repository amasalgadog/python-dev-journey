'''
Exercise 5-1
Finding the largest number with a sequence of numbers using a 'for' loop

'''

max = 0
n_list = [9, 41, 12, 3, 74, 15]
for n in n_list:
    if n > max:
        max = n
print(max)