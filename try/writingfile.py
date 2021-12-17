data = open('file.txt','w')
print(data)
line3 = "This is1 my second line wrote by me.\n"
data.write(line3)
data.close() #When you are done writing, you have to close the file to make sure that the last bit of data is physically written to the disk so it will not be lost if the power goes off.