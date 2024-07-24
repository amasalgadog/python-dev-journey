import xml.etree.ElementTree as ET
#   ET will work as an alias for the library imported

input = '''<stuff>
    <person>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </person>
</stuff>'''
#   the triple quoted string is a multiple line string, and
#   the input will be the data to parse

stuff = ET.fromstring(input)
#   fromstring will parse de string data in input in the form of a tree node
lst = stuff.findall('person/user')
#   findall will return a list of all the tags that follows the path given
print('User count:', len(lst))

for item in lst:
    print()
    print('Name', item.find('name').text)
    #   find will return the node representing the 'name' tag and .text will specify that the information returned is located between the tags
    print('Id', item.find('id').text)
    #   same as previous
    print('Attribute', item.get('x'))
    #   .get will look for the attritute 'x' and return its value

    #   so, find works for single tags search and findall works for multiple tags search