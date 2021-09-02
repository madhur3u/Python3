from sys import argv
script, filename = argv
# taken file input in script

def print_all(f): # fn to read a file
    print(f.read())

def rewind(f): # fn to place file pointer at 0 or start
    f.seek(0)

def print_a_line (line_number, f): # fn to read one line at a time
    print(line_number,'\t', f.readline(), end='')

# readline always returns the \n too so we use end='' here so that there is no
# gap between lines 

#main

# readline() is code that scans each byte of the file until it finds a \n character,
# then stops reading the file to return what it found so far

file1 = open(filename)

print_all(file1) # print whole file by calling fn
rewind(file1)    # will take us to starting pos of file1

print('Now we will print all lines seprately')
ln = 1           # this indicates the line_number
print_a_line(ln, file1)     # print the 1 st line
ln = ln + 1
print_a_line(ln, file1)     # print 2nd line and so on...
ln += 1                     # SHORTHAND NOTATION means ln = ln + 1 only
print_a_line(ln, file1)
ln += 1
print_a_line(ln, file1)
