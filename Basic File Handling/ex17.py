from sys import argv
from os.path import exists

# You should immediately notice that we import another handy command named exists . This returns
# True if a file exists, based on its name in a string as an argument. It returns False if not.

script, from_file, to_file = argv
print(f'Copying data from {from_file} to {to_file}')

# if the to_file in which we are writing do not exists then it will create a new file with the name
# we give in script

file1 = open(from_file)
data = file1.read()

# data = open(from_file).read() this will read the file in one line and close the file immediately
# after eading. So no need of closing the from_file here.

print(f'Input file is {len(data)} bytes long')

# What does the len() function do? It gets the length of the string that you pass to it then returns that
# as a number.

print(f'Does the output file exists? {exists(to_file)}') # to check if to_file exist using exists
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

print('Writing into OUTPUT file now...')

file2 = open(to_file, 'w') # in 'w' mode it will delete all data from file if it exist and write from start
file2.write(data)

print('\nWRITING COMPLETE')

file1.close()
file2.close()

# madhur3u@ZorinMadhur:~/Desktop/Python3$ cat file.txt
# cat file.txt
# writing this in terminal will OUTPUT the file in terminal
