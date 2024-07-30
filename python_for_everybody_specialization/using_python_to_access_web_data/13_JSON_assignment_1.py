'''

Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2049594.json (Sum ends with 72)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Data Format

The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at xml3.py to see how to prompt for a URL and retrieve data from a URL.

'''

import urllib.request, urllib.parse
import ssl, json

url_sample = 'http://py4e-data.dr-chuck.net/comments_42.json'
url_actual = 'http://py4e-data.dr-chuck.net/comments_2049594.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = list()

url_handle = urllib.request.urlopen(url_actual, context=ctx)
data = url_handle.read().decode()

# print(data)

try:
    info = json.loads(data)
except:
    info = None

# print(info)
# print(type(info))

# print(info['comments'])

size = len(info['comments'])
i = 0

while i < size:
    
    count.append(info['comments'][i]['count'])
    i += 1


print('Sum:', sum(count))