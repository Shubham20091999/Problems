# https://www.hackerrank.com/challenges/pairs/problem

from collections import Counter

n,k=map(int,input().split())
freq=Counter(map(int,input().split()))
count=0
for num in freq:
    count+=freq[num]*freq[num+k]

print(count)

n,k=map(int,input().split())
freq=sorted(list(map(int,input().split())))

tail=0
head=1
count=0
while head<n:
    diff=freq[head]-freq[tail]

    if(diff==k):
        count+=1
        head+=1
    elif(diff<k):
        head+=1
    else:
        tail+=1
print(count)