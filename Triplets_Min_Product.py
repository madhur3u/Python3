# Given an array of Int find min product among all triplets combinations

a = list(map(int, input().split()))
a.sort()
p1 = a[0]*a[1]*a[2]
p2 = a[0]*a[-1]*a[-2]
print(min(p1,p2))
