'''

Assignment 6.5 
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.

Desired Output: 
0.8475

'''

text = "X-DSPAM-Confidence:    0.8475"
pos_prefix = text.find(' ')
new_text = text[pos_prefix:]
s_value = new_text.strip()
f_value = float(s_value)
print(f_value)