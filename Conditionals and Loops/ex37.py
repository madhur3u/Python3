print('Hi bye First\rProgram')
print('Hello World')
print('Adachi to Shimamura\fis best Yuri LN')
print('Y\vuri is life')
print('Sayonara')

# \b backspace
# \f formfeed do the print like this 'Adachi to Shimamura
#                                                        is best Yuri LN'
# \r carriage
# \v vertical tab quite like formfeed 

s = lambda a : a + 10 * a ** 2 # lambda works like a short function
print(s(5))

print('%x' % 1000) # print hexadecimal of 1000 or number with lowercase
print('%X' % 1000) # hxd uppercase
print('%o' % 16) # octal number
print('%c' % 97) # give the character for the ASCII value
print('%e' % 1456896) # exponent notation
print('%E' % 786896) # exponent notation E UPPERCASE
