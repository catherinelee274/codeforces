
import sys
input = sys.stdin.readline


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def foo(s): 
    # if there are at least 7 players of the same team standing one 
    # after the other , then situation is dangerous 

    # can do in O(n)
    prev = None 
    cnt = 1  
    isdangerous = False 
    for i in range(len(s)): 
        if not prev or s[i] != prev:
            prev = s[i] 
            cnt = 1 

        else: 
            cnt += 1 
            prev = s[i] 

            if cnt == 7:
                isdangerous = True
                break 

    if isdangerous:
        print('YES')
    else:
        print('NO')


s = insr() 
foo(s) 

# foo('00100110111111101')
# foo('11110111011101')