# FILE HANDLING

from sys import argv
script, filename = argv

# rather than taking input inside our code we are taking the filename as script
# input from the user

txt = open (filename) # txt is now object of our file
print ('This was your filename : ', filename)
print (txt.read()) # reading whole file here

# traditional way of opening a file by using the CODE to input filename

print ('Enter filename again')
fn = input('>>\t')
txt1 = open (fn) # new object

print (txt1.read())

# we can open one files two time in a code without closing it 1st like we did
# here, we made 2 objects for the same file.
