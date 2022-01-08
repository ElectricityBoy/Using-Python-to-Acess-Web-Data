import urllib.request , urllib.parse , urllib.error

fhand = urllib.request.urlopen( 'https://en.wikipedia.org/wiki/List_of_Hunter_×_Hunter_characters#Killua_Zoldyck')
for line in fhand:
    print(line.decode().strip())