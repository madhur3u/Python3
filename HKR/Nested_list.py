# https://www.hackerrank.com/challenges/nested-list/problem

name =[]
score =[]
for _ in range(int(input())):
    name.append(input())
    score.append(float(input()))

x = list(set(score))
x.sort()
m2 = x[1]

s =[]
for i,j in zip(score,name):
    if i == m2 : s.append(j)
    
s.sort()
for t in s : print(t)

# a = [[input(), float(input())] for i in range(int(input()))]
# s = sorted(set([x[1] for x in a]))
# for name in sorted(x[0] for x in a if x[1] == s[1]):
#     print name
