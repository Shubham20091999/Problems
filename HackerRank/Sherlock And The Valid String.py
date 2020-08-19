# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

counter=Counter(list(Counter(list(input())).values()))
base=counter.most_common()[0][0]
counter.pop(base)

if(len(counter)==0):
    print('YES')
    exit(0)

if(len(counter)==1):
    val=list(counter.keys())[0]
    if(counter[val]==1):
        if(val==1):
            print('YES')
            exit(0)
        elif(val-base==1):
            print('YES')
            exit(0)
print('NO')

# ------------------------------------

from collections import Counter

counter=list(Counter(list(input())).values())

numOf1=0
num1=-1
for num in counter:
    if(num==1):
        numOf1+=1
        num1=num

if(numOf1==1):
    counter.remove(num1)
    try:
        base=min(counter)
    except:
        base=None
    for num in counter:
        if(num>base):
            print('NO')
            exit(0)
    print('YES')

else:
    base=min(counter)
    numGreater=0

    for num in counter:
        if(num>base):
            numGreater+=(num-base)
            if(numGreater>=2):
                print('NO')
                exit(0)

    print('YES')