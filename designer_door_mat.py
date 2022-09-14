import math
N = int(input())
if N % 2 != 0:
    M = N * 3
    h = '-'
    d = '.'
    p = '|'
    design = f'{d}{p}{d}'
    for i in range(N):
        if i == 0:
            continue
        elif i % 2 != 0:
            print((design*(i)).center(M, '-'))

    for i in range(N,0,-1):
        if i == N:
            print('WELCOME'.center(M, '-'))
        elif i % 2 != 0:
            print((design*(i)).center(M, '-'))
