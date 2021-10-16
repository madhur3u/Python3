# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    # your code goes here
    K_substr = 0    # count of all the substrings to be formed by Kevin, of vowels
    S_substr = 0    # count of all the substrings to be formed by Stuart, of consonants
    
    n = len(s)      # this will have length of our string
    
    for i in range(n):  # iterating in string
        
        # if character is a vowel
        # we will add all the substrings starting from that vowel in the letter
        # this is equal to no. of letters left from vowel till end (see end example)
        # like this we will get no. of substrings starting from that point
        # and since we are accounting for all substrings starting from vowel in that word
        # we will have all repetitions in the count, so no need to do anything extra for that
        if s[i] in ['A', 'E', 'I', 'O', 'U']:
            K_substr += (n - i)
        
        # same as above 
        else:
            S_substr += (n - i)
    
    # checking count and print acc to question
    if K_substr > S_substr:
        print('Kevin', K_substr)
    elif S_substr > K_substr:
        print('Stuart', S_substr)
    else:
        print('Draw') 

# main code
s = input()
minion_game(s)

# For the word "BANANA", the first vowel 'A' occurs at position 1, len("BANANA") = 6, 
# so there are 6-1 = 5 substrings starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], --> 1 is the value of i
# you add one extra letter to that specific letter 'A' until you get to the end of the word.
