# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

from collections import Counter

# Median Using Count Sort
# This is better because exp<=200
def getMedian(counter: Counter, d):
    tmp = 0
    if(d % 2 != 0):# if d is odd
        for n in sorted(counter.keys()):
            tmp += counter[n]
            if(tmp > d/2):
                return n
    else:# if d is even
        prevNum = 0
        for n in sorted(counter.keys()):
            tmp += counter[n]
            if(tmp > d//2):
                if(tmp-counter[n] == d/2):
                    return (n+prevNum)/2
                else:
                    return n
            prevNum=n

n, d = map(int, input().split())
exp = list(map(int, input().split()))

counter = Counter(exp[:d])
count = 0
for i in range(d, len(exp)):
    med = getMedian(counter, d)
    if(exp[i] >= med*2):
        count += 1
    counter[exp[i-d]] -= 1
    counter[exp[i]] += 1

print(count)
