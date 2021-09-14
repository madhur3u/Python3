# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/

def EXPONENTIATION(x,y,p):
    res = 1 # this will be our result initial value 1
    x = x % p # updating x 
    if (x == 0 ) : return 0

    while y > 0 :

        if y % 2 != 0 : # for y odd we will update res
            res = (res*x) % p
        
        y = y//2
        x = (x*x) % p
    
    return res

x,y,p = map(int,input().split())
# to find (x**y)%p
# RUSSIAN PEASENT EXPONENTIATION METHOD

print(EXPONENTIATION(x,y,p))
