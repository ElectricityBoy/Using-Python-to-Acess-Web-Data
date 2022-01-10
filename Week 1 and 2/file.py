file = open('regular.txt','r')
print(file)
#When we called a file, the program will print the file handle. It's basicaly a answer if the file exist;
counter = 0
for line in file:
    line = line.rstrip() #this method strips whitespace from of a string
    if line.startswith('From:'):  
        print(line)

print('-='*20 )

#Another way to find what you searching for is using the find string method.

for line in file:
    line = line.rstrip()
    if line.find('david')== True: continue
print(line)