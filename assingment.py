import re

file = open('teste2.txt','r')
soma = 0

for line in file:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for i in x:
        soma = soma + int(i)

print(soma)