# URL - http://py4e-data.dr-chuck.net/comments_1433568.html
#This assingment requires find all spam tags and them sum all number of this tag using bs4

#Importing libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')
soma = 0
# Retrieve all of the span tags
tags = soup('span')
x = list()
for tag in tags:
    for i in tag:
        x = re.findall('[0-9.]+', i.rstrip())
        for u in x:
            soma = soma + int(u)

print(soma)