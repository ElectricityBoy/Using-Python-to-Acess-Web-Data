#In this exercise i have to read a file and register every number. Then the program have to sum the numbers and print the result.
import re
#Importing the regular expression library
file = open('teste2.txt','r')
#Opening the text file
soma = 0

for line in file:
    line = line.rstrip()
    #The rstrip() method will remove the trailing characters
    x = re.findall('[0-9]+', line)
    #This line line will find in the variable line any number of one or more digits
    for i in x:
        soma = soma + int(i)
    #Then in this repetition loop, it will sum the number who are find before

print(soma)