# https://www.hackerrank.com/challenges/python-time-delta/problem

# n this challenge, our goal is the first convert the time stamp to UNIX time stamps that
# are independent of timezones. After that we simply subtract and print the difference.
# To solve this in python you can use the python package called datetime and it has a 
# function called strptime. Using which we can get a time object.

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# This tool returns a date time corresponding to a date string, parsed according to format.

from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    
    i1 = dt.strptime(input(), fmt)
    i2 = dt.strptime(input(), fmt)
    
    print(int(abs(i2 - i1).total_seconds()))
    
    
