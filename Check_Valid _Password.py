'''
A password is a string of characters which
is valid only when it contains atleast one numerical character, atleast one lowercase
english alphabet character and atleast one uppercase english alphabet character.
Geek is too smart to do this job manually, so he decided to make a program to
automate the process. Help him write a program which when given a string S (the
password) prints "YES" if it is a valid password or "NO" otherwise.
Input Format:
1. The 1rst line of the input contains a single integer T denoting the number of test
cases.
2. The 1rst line of each test case contains a single string S.
Output Format:
For each test case, print "YES" or "NO" in a new line.
'''

n = int(input())
for j in range(n) :
    a = 0; b = 0; c = 0
    f = False
    s = input()
    for i in range(len(s)):
        
        if (s[i].isupper() == True) : 
            a += 1 
            
        elif (s[i].islower() == True) : 
            b += 1
          
        elif (s[i].isnumeric() == True) : 
            c += 1
                
        if(a>0 and b>0 and c>0): 
            f = True
            break
            
    if f == True : print('YES')
    else : print('NO')
