import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

link = 'http://py4e-data.dr-chuck.net/comments_1433570.xml'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(link, context=ctx).read()

tree = ET.fromstring(html)
lst = tree.findall('comments/comment')

print('Retrieving: ', link)
print('Characters: ', len(html))
x = 0
for item in lst:
    x += int(item.find('count').text)

print('Count sum :' , x)

   

    
