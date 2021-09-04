import sys
script, encoding, error = sys.argv
# 1 and 2 are use to take input just like we used earlier but here argv assigned in 2nd line

def main(language_file, encoding, errors): # made a fn to be called at end of code taking file and other inputs
    line = language_file.readline() # this is just reading one line using readline from language_file

    if line : # work if line has something in it so it give TRUE to if statement
        print_line(line, encoding, errors) # printing a line by calling fn print_line
        return main(language_file, encoding, errors) # calling fn main inside main again to form a kind of loop
# the fn main will run till whole file is over as soon as if st gets false so file ends and main fn will also terminate

def print_line(line, encoding, errors): # fn responsibe for encoding and printing
    next_lang = line.strip() # This is a simple stripping of the trailing \n on the line string and storing in next_lang
    raw_bytes = next_lang.encode(encoding, errors=errors) # encoding string we take from 1st line of language_file
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decoding the code stored in raw bytes

    print(raw_bytes, "<===>", cooked_string)

# main program calling fn and opening file
languages = open("languages.txt", encoding = "utf-8") # encoding utf8 to use it in that encoding

main(languages, encoding, error) # calling fn main


# [14] when we readline we also get \n in the line so if we want to remove the \n from the line which we have read
# we can do line.strip() this will strip the \n from the line we have read in 'line' variable

# [16] This string should be the same as the next_lang variable
''' OUTPUT
$ python3.6 ex23.py utf-8 strict
b'Aragon\xc3\x83\xc2\xa9s' <===> AragonÃ©s
b'Aragon\\xc3\\x83\\xc2\\xa9s' <===> Aragon\xc3\x83\xc2\xa9s
b'0101110' <===> 0101110
'''
