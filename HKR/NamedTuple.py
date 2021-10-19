# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())

fields = input()  # ID MARKS NAME CLASS --> this will be in fields
student = namedtuple('student', fields) # make a named tuple of fields

marks = 0   

for _ in range(n):
    
    i1, i2, i3, i4 = input().split()    # input fields value for each student
    s1 = student(i1, i2, i3, i4)        # place it in named tuple now can be called using fields
    marks += int(s1.MARKS)              # add the marks
    
print(marks/n)  # average
