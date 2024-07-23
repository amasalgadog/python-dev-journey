import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#   importing the sockets library and the beautifulsoup library (previously installed)

url = 'https://amasalgadog.github.io/odin-recipes/'
html = urllib.request.urlopen(url).read()
#   read() put all the data recovered from 'url' in a single string

soup = BeautifulSoup(html, 'html.parser')
#   BeautifulSoup() will parse the the info by 'html.parser'

tags = soup('a')
#   this will create a list with any of the tags inside the founction soup(), in this case the anchor tag 

#   print(tags) -> yep, tags is definetely a list of anchor HTML elements
for tag in tags:
    print(tag)
    #   get the tag from the HTML element

    print(tag.get('href', None))
    #   get the link from the href attribute in the anchor element
    
    print(tag.contents[0])
    #   get the content from the HTML element

    print(tag.attrs)
    #   get the attributes in the HTML anchor element

    print()

#   the print should return 'http://www.dr-chuck.com/page2,htm'