line = 'From elder.guedes@hotmail.com dez-15-2020'

words = line.split()
#When we use the split method, it will create a list of words that contain the words
print(words)

email = words[1].split('@')
#When we use the split method, it will create a list of words that contain parts separated by what you define 
print(email[1])
