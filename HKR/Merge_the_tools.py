# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(s, k):
    # your code goes here
    for i in range(0,len(s),k):       # run loop in intervals of k
    
        sub = s[i:i + k]              # take the substring
        ans = ''                      # empty string to store ans

        for j in range(k):            # iterate in substring
            if sub[j] not in ans :    # since no repeated elements
                ans = ans + sub[j]
        
        print(ans)

# main
string, k = input(), int(input())
merge_the_tools(string, k)
