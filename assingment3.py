import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter URL: ')
count = int(input('Counter: '))
position = int(input('Position: '))
counter = 1

a = True

while a == True:
    control = 0
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    for tag in tags:
        control +=1
        if (control == position) :
            print('Retrieving : ' , tag.get('href', None))
            url = tag.get('href', None)
    
    if (counter == count):
        a = False
    else:
        counter += 1
    

