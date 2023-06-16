string1 = 'text'

# opening a text file
file1 = open("sensitive_words.txt", "r")

# read file content
readfile = file1.read()

# checking condition for string found or not
if string1 in readfile:
    print('String', string1, 'Found In File')
else:
    print('String', string1, 'Not Found')

# closing a file
file1.close()