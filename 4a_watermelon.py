# https://codeforces.com/problemset/problem/4/A

# 1 <= w <= 100 

import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))

val = inp()

if val == 2: 
    print('NO')
elif val%2 == 0: 
    print('YES')
else:
    print('NO')

