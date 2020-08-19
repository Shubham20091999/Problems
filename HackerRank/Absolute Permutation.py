# https://www.hackerrank.com/challenges/absolute-permutation/problem?h_r=internal-search
for i in range(int(input())):
    n, k = map(int, input().split())
    if(k == 0):
        print(list(range(1, n+1)))
    elif(n % (2*k) != 0):
        print(-1)
    else:
        for i in range(0, n // (2*k)):
            for j in range(1, k+1):
                print(j+k+i*2*k, end=' ')
            for j in range(1, k+1):
                print(j+i*2*k, end=' ')
