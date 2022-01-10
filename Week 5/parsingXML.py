import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
        <phone type="intl">
        +1 734 303 4456
        </phone>
        <email hide="yes" />
</person>'''
tree = ET.fromstring(data)
#Calling fromstring converts the string representation of the XML into a “tree” of XML elements
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))