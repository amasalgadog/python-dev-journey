import urllib.request, urllib.parse
import http, json, ssl

# heavily rate limited proxy of http://www.geopify.com api
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    print()
    if len(address) < 1: break
    # break loop if address doesn't any character

    address = address.strip()
    # address striped from any whitespace (left or right)

    parms = dict()
    parms['q'] = address
    # 'q' is the query defined by the address, given to the proxy 'serviceurl'

    url = serviceurl + urllib.parse.urlencode(parms)
    # 'url' is the full URL, proxy + the query of the location encode for url

    print('Retrieving:', url)
    print()
    urlhandle = urllib.request.urlopen(url, context=ctx)
    # create a handle for the URL ignoring the ssl certificate errors

    data = urlhandle.read().decode()
    # decode() make sure urlhandle it's UTF-8 and then give 'data' a python string (unicode) of the URL handle
    # 'data' is being decode into a string in JSON serialization format = Raw Data
    
    print('Retrieved:', len(data), 'characters.', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
        # parsing the data > string into format (collection type)
    except:
        js = None

    # sanity check for Features
    # making sure Features key exists in the js dictionary
    if not js or 'features' not in js:
        print('=== Download Error ===')
        print(data)
        break

     # making sure Features has something
    if len(js['features']) == 0:
        print('=== Object not found ===')
        print(data)
        break

    print(json.dumps(js['features'], indent=2))
    # dumps convert Python primitive types into JSON equivalent
    # indent format the way the data is shown - add indentation
    print()

    # Features is an array and we need to access the first element inside it
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    # look up for 'lat' and 'lon' key's values and saved them
    print('lat', lat, 'lon', lon)
    print()

    location = js['features'][0]['properties']['formatted']
    # look up for 'formatted' key's value and saved it kin 'location'
    print(location)
