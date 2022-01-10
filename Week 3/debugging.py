import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
#In this regular expression, it will find the phrase who start with F and ends with :
print(y)