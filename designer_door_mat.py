import math
N, M = input().split()
if int(N) % 2 != 0:
    # M = N * 3
    h = '-'
    d = '.'
    p = '|'
    design = f'{d}{p}{d}'
    for i in range(int(N)):
        if i == 0:
            continue
        elif i % 2 != 0:
            print((design*(i)).center(int(M), '-'))

    for i in range(int(N),0,-1):
        if i == int(N):
            print('WELCOME'.center(int(M), '-'))
        elif i % 2 != 0:
            print((design*(i)).center(int(M), '-'))
