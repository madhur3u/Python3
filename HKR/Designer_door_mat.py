n, m = map(int, input().split())

dash = (m - 3) // 2                                                     # initializing dash acc to pattern
dash_mid = (m - 7) // 2                                                 # dash in middle row one side
dot = 1                                                                 # middle pattern initially 1

for i in range(1,n + 1):

    if i < (n//2 + 1) :                                                 # for 1st half
        print ( (dash * '-') + ('.|.' * dot) + (dash * '-') )
        dash = dash - 3                                                 # dash decrease and middle dots increase
        dot = dot + 2
    
    elif i == (n//2 + 1) :                                              # for miidle row
        print ( (dash_mid * '-') + ('WELCOME') + (dash_mid * '-') )     

    else :
        dash = dash + 3
        dot = dot - 2
        print ( (dash * '-') + ('.|.' * dot) + (dash * '-') )           # for bottom row
