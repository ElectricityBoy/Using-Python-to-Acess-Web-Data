try:
    fhand = open('regular.txt')
except:
    print('File cannot be opened:', 'fname')
    exit()
count = 0
for line in fhand:
    if line.startswith('David:'):
        count = count + 1
print('There were', count, 'subject lines in',' fname')