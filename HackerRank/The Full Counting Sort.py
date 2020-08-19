# https://www.hackerrank.com/challenges/countingsort4/problem
lst = [[] for _ in range(100)]

n = int(input())

for i in range(n):
    x, s = input().split()
    x = int(x)

    if(n/(i+1) >= 2):
        lst[x].append('-')
    else:
        lst[x].append(s)

for li in lst:
    if(len(li)!=0):
        print(' '.join(li),end=' ')

# -----------------------------
lst = {}
n = int(input())

for i in range(n):
    x, s = input().split()
    x = int(x)

    if(n/(i+1) >= 2):
        if(x in lst):
            lst[x].append('-')
        else:
            lst[x]=['-']
    else:
        if(x in lst):
            lst[x].append(s)
        else:
            lst[x]=[s]

for li in sorted(lst.keys()):
    print(' '.join(lst[li]),end=' ')

