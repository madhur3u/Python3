from collections import namedtuple

n = int(input())

fields = input().strip().split()        # ID MARKS NAME CLASS --> this will be in field
student = namedtuple('student', fields) # make a named tuple of fields

marks = 0   

for _ in range(n):
    
    i1, i2, i3, i4 = input().strip().split()    # input fields value for each student
    s1 = student(i1, i2, i3, i4)                # place it in named tuple now can be called using fields
    marks += int(s1.MARKS)                      # add the marks
    
print(marks/n)  # average
