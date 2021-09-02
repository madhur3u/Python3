# READING AND WRITING FILES
''' FILE COMMANDS
    • close – Closes the file. Like File->Save.. in your editor.
    • read – Reads the contents of the file. You can assign the result to a variable.
    • readline – Reads just one line of a text file.
    • truncate – Empties the file. Watch out if you care about the file.
    • write('stuff') – Writes ”stuff” to the file.
    • seek(0) – Move the read/write location to the beginning of the file.
'''

from sys import argv
script, filename = argv # taking input of filename in script

print('We are going to erase the given file ', filename)
print('Hit Ctrl + C to stop')
print('Hit Enter to continue')

input('???')

print('Opening the file ...')
file1 = open (filename, 'w')

print('Truncating the file in 3..2..1..')
file1.truncate() # empty the file

print('Now your file is empty, input 3 lines for the file now')
line1 = input('Line 1 :\t')
line2 = input('Line 2 :\t')
line3 = input('Line 3 :\t')

file1.write(line1) # writing in file can write directly in brackets or use variables
file1.write('\n')
file1.write(line2)
file1.write('\n')
file1.write(line3)
file1.write('\n')

print('File Closed')
file1.close() # closing a file

'''
What does 'w' mean? It’s really just a string with a character in it for the kind of mode for the file. If
you use 'w' then you’re saying ”open this file in ’write’ mode,” thus the 'w' character. There’s
also 'r' for ”read,” 'a' for append, and modifiers on these.

'w+' , 'r+' , and 'a+'

Does just doing open(filename) open it in 'r' (read) mode

'''
