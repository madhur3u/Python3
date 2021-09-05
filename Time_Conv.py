# Given a time in 12 -hour AM/PM format, convert it to military (24-hour) time. 
# https://www.hackerrank.com/challenges/time-conversion/problem

t = input()
a = t[8:10]
b = int(t[0:2])

if a == 'AM' and b != 12 : print(t[0:8])
else :
    if b == 12 and a == 'PM' : print(t[0:8])
    else :
        b = b + 12
        if b == 24 : b = '00'
        else : b = str(b)
    
        time = b + t[2:8]
        print(time)
