# Given a number n construct a string of length n using lowercase such that
# each substring in that occurs odd number of times
# n <= 10**5  
# PARITY OF PERMUTATIONS

# LOGIC : 
# even + odd = odd is the main logic used here
# taking n = 10
# creating half string with same characters --> a a a a a
# here in this if we check occurence of all substrings we have
# aaaaa --> 1
# aaaa  --> 2
# aaa   --> 3
# aa    --> 4
# a     --> 5 

# aaaa, aa occurs even time so we have to make it odd
# now consider one more string with n/2 -1 characters  --> a a a a
# checking substrings
# aaaa  --> 1
# aaa   --> 2
# aa    --> 3
# a     --> 4
# here we have aaaa, aa odd 

# so we combine both of them together and we have all substrings odd 
# as n/2 and n/2 - 1 has consecutive odd even substrings count so if we add all together
# all substrings count will become odd
# aaaaa --> 1 + 0 = 1
# aaaa  --> 2 + 1 = 3
# aaa   --> 3 + 2 = 5
# aa    --> 4 + 3 = 7
# a     --> 5 + 4 = 9       

# so to combine them we add a seprator in between which can be any alphabet say b
# so our final ans is --> aaaaabaaaa --> which has all odd substrings

# for odd add 2 seprators 

def oddSubString(n):

    # corner case
    if n == 0 : return ''
    if n == 1 : return 'a'
    
    # for even, 1 seprator 
    if n % 2 == 0 :
        return ('a' * (n//2)) + 'x' + ('a' * (n//2 - 1))

    # for odd, 2 seprators
    else :
        return ('a' * (n//2)) + 'xy' + ('a' * (n//2 - 1))


n = int(input())
print(oddSubString(n))
