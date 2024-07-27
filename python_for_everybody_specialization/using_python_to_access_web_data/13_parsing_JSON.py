import json

input = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456" },
    "email" : {
        "hide" : "yes" }    
}'''

info_dict = json.loads(input)
#   loads() will parse the string 'input' into a dictionary, because 'input' format is one of dictionary

print('Parsing dictionary: ', info_dict)
print()
print(info_dict['name'])
print(info_dict['email']['hide'])

data ='''[
{   "id" : "001",
    "x" : "2",
    "name" : "Chuck" },
{   "id" : "009",
    "x" : "7",
    "name" : "Jeff" }   
]'''

info_lst = json.loads(data)
#   loads() will parse the string 'data' into a list, because 'data' format is one of list

print()
print('Parsing list: ', info_lst)
for item in info_lst:
    print()
    print(item['name'])
    print(item['id'])
    print(item['x'])